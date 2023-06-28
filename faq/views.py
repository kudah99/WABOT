from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import redis
import random
from twilio.twiml.messaging_response import MessagingResponse
from .models import FAQ

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_next_fqa(usernumber):
    last_fqa = r.get(usernumber)
    if last_fqa:
        last_fqa = int(last_fqa.decode('utf-8'))
    else:
        last_fqa = -1
    fqa_list = list(FAQ.objects.all().values_list('id', flat=True))
    remaining_fqa_list = set(fqa_list) - set(range(last_fqa + 1))
    if remaining_fqa_list:
        next_fqa_id = random.choice(list(remaining_fqa_list))
        r.set(usernumber, next_fqa_id)
        return FAQ.objects.get(id=next_fqa_id)
    else:
        r.delete(usernumber)
        return None

def faq_handler(request):
    if request.method == 'POST':
        twilio_request = request.POST
        user_id = twilio_request.get('From')
        cache_key = user_id+"fqa"
        fqa = get_next_fqa(cache_key)
        if fqa:
            response = MessagingResponse()
            response.message(f"_{fqa.faq_question}_\n\n{fqa.answer}\n\nTo continue, reply with 1. To return to the main menu, reply with 0.")
            return HttpResponse(str(response))
        else:
            response = MessagingResponse()
            response.message("There are no more FAQs available. Please try again later.")
            return HttpResponse(str(response))
    else:
        return HttpResponse("This is a webhook endpoint.")