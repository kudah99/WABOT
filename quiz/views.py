import random

from django.core.cache import cache
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

from .models import Trivia


def trivia_game(request):
    incoming_msg = request.POST['Body'].strip().lower()
    user_phone = request.POST['From']

    response = MessagingResponse()
    msg = response.message()

    questions = cache.get(f'{user_phone}:random_questions')
    last_question_answer = cache.get(f'{user_phone}:expected_answer')
    last_score = cache.get(f'{user_phone}:score', 0)

    if not questions:
        all_questions = list(Trivia.objects.all())
        random.shuffle(all_questions)
        questions = all_questions[:15]
        cache.set(f'{user_phone}:random_questions', questions, 600)

    if questions:
        question = questions[0]
        if not last_question_answer:
            set_cache(user_phone, question.answer)
            msg.body(f"Question: {question.question}\nReply with 'True' or 'False'")
        elif last_question_answer == incoming_msg:
            set_cache(user_phone, question.answer)
            msg.body(f"Question: {question.question}\nReply with 'True' or 'False'")
            cache.set(f'{user_phone}:score', last_score+1, 600)
            questions.pop(0)
            cache.set(f'{user_phone}:random_questions', questions, 600)
        elif last_score != incoming_msg:
            set_cache(user_phone, question.answer)
            questions.pop(0)
            cache.set(f'{user_phone}:random_questions', questions, 600)
    else:
        score_percentage = (last_score / 15) * 100
        msg.body(f"Quiz completed!! Your score is {score_percentage}%\n\n Reply with *0* to return to the main menu.")

    return HttpResponse(str(response))


def set_cache(user_phone, expected_answer):
    cache.set(f'{user_phone}:expected_answer', expected_answer, 600)
    cache.set(f'{user_phone}:score', cache.get(f'{user_phone}:score', 0), 600)