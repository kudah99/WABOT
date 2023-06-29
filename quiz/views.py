import random

from django.core.cache import cache
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .models import Trivia
from WABOT.settings import AccountSID,AuthToken

terminate ='Replay with 0 to return to home.'
client = Client(AccountSID, AuthToken)
space = " "
def trivia_game(request):
    incoming_msg = request.POST['Body'].strip().lower()
    user_phone = request.POST['From']
    my_numbber = request.POST['To']
    from_number = user_phone[9:]
    print(from_number)
    to_number =my_numbber[9:]
    print(to_number)

    response = MessagingResponse()
    msg = response.message()

    questions = cache.get(f'{user_phone}:random_questions')
    last_question_answer = cache.get(f'{user_phone}:expected_answer')
    last_score = cache.get(f'{user_phone}:score', 0)

    if not questions and last_score == 0:
        all_questions = list(Trivia.objects.all())
        random.shuffle(all_questions)
        questions = all_questions[:10]
        cache.set(f'{user_phone}:random_questions', questions, 600)

    if questions:
        question = questions[0]
        if not last_question_answer:
            set_cache(user_phone, question.answer)
            send_msg(msg=f"Question: {question.question}. {terminate}",FROM=to_number,TO=from_number)
        elif last_question_answer == incoming_msg:
            set_cache(user_phone, question.answer)
            send_msg(msg="Correct answer ✔️",FROM=to_number,TO=from_number)
            send_msg(msg=f"Question: {question.question}. {terminate}",FROM=to_number,TO=from_number)
            cache.set(f'{user_phone}:score', last_score + 1, 600)
            questions.pop(0)
            cache.set(f'{user_phone}:random_questions', questions, 600)
        else:
            # Incorrect answer  
            set_cache(user_phone, question.answer)
            questions.pop(0)
            cache.set(f'{user_phone}:random_questions', questions, 600)
            send_msg(msg=f"Incorrect answer. The correct answer is *{last_question_answer}*",FROM=to_number,TO=from_number)
            send_msg(msg=f"Question: {question.question}. {terminate}",FROM=to_number,TO=from_number)
    else:
        score_percentage = (last_score / 10) * 100
        delete_cached_data(user_phone=user_phone)
        msg.body(f"Quiz completed!! Your score is *{score_percentage}%*. You can retake the game and receive new challenges.\n\n Reply with *0* to return to the main menu.")

    return HttpResponse(str(response))

def send_msg(msg,FROM,TO):
    message = client.messages \
    .create(
         body=msg,
         from_=f'whatsapp:{FROM}',
         to=f'whatsapp:{TO}'
     )
    print(message.sid)

def set_cache(user_phone, expected_answer):
    cache.set(f'{user_phone}:expected_answer', expected_answer, 600)
    cache.set(f'{user_phone}:score', cache.get(f'{user_phone}:score', 0), 600)

def delete_cached_data(user_phone):
    cache.delete(f'{user_phone}:random_questions')
    cache.delete(f'{user_phone}:expected_answer')
    cache.delete(f'{user_phone}:score')