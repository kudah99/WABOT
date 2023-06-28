from datetime import datetime, timedelta

from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from faq.views import faq_handler
from response_messages.models import ResponseMessages
from main_menu.models import MainMenu
from political_parties.models import Political_Parties
from elections_candidates.models import PresidentialCandidates, MemberOfParliamentCandidates
from prettytable import PrettyTable as pt
from twilio.twiml.messaging_response import MessagingResponse
from wa_user.models import WAUsers
from quiz.views import trivia_game


EXPIRATION_TIME = 5 # In minutes

# Constants for current action keys
CURRENT_ACTION_PREFIX = "action"
MAIN_MENU_ACTION = "main_menu"
QUIZ_ACTION = "quiz"
FIND_MP_ACTION = "find_mp"
FAQ_ACTION = "faq"
emoji_code_points = {
    1: '1️⃣',  
    2: '2️⃣',
    3:'3️⃣',
    4:'4️⃣',
    5:'5️⃣',
    6:'6️⃣',
    7:'7️⃣',
    8:'8️⃣',
    9:'9️⃣'
}

@csrf_exempt
def inbound(request):
    number = request.POST.get('From')
    message_body = request.POST.get('Body').strip().lower()
    user_number = number[9:]

    if user := cache.get(user_number):
        if user.user_name is None:
            qnumber = WAUsers.my_objects.get(phone_number=user_number)
            qnumber.user_name = message_body
            qnumber.save() 
            add_user_to_cache_DB(phonenumber=user_number, user=qnumber)
            return send_main_menu(phone_number=user_number)
        
        current_action = cache.get(f"{CURRENT_ACTION_PREFIX}{user_number}")
        if  current_action== None:
            return send_main_menu(phone_number=user_number)
        elif current_action == MAIN_MENU_ACTION:
            if message_body == "1":
                add_current_action_to_cache_DB(phoneNumber=user_number,value="quiz",expire_at=15)
                _msg = f"Do you wish play quiz game to test you knowledge about Zimbabwe elections.\n\n Reply with *1* to start quiz game now or *0* to return to the main menu."
                return send_response_messages(msg=_msg)
            elif message_body == "2":
                return send_political_parties(phone_number=user_number)
            elif message_body == "3":
                return send_presidential_candidates(phone_number=user_number)
            elif message_body == "4":
                return send_mp_start(phone_number=user_number)
            elif message_body == '5':
                add_current_action_to_cache_DB(phoneNumber=user_number,value=FAQ_ACTION,expire_at=5)
                return faq_handler(request=request)
        elif current_action == QUIZ_ACTION:
            if message_body  in ['1','true','false']:
                return trivia_game(request=request)
            elif message_body == "0":
                return send_main_menu(phone_number=user_number)
            else:
                invalid_reply()
        elif current_action == FIND_MP_ACTION:
            return send_mp_end(phone_number=user_number,constituency_name=message_body)
        elif current_action == FAQ_ACTION:
             if message_body  in ['1']:
                    return faq_handler(request=request)
             elif message_body== "0":
                        return send_main_menu(phone_number=user_number)
             else:
                 _msg = """
                        Invalid response. You currently reading fqa. To terminate game reply with *0*
                        """
                 return send_response_messages(msg=_msg)

    _reply = ResponseMessages.objects.get(pk=1)
    reply = f"*Hey Buddy!* 😀 Welcome !! {user_number} to ballot buddies.\n\n {_reply.en_text}"
    try:
        qnumber = WAUsers.my_objects.get(phone_number=user_number)
        add_user_to_cache_DB(phonenumber=user_number, user=qnumber)

        if qnumber.user_name is None:
            return send_response_messages(msg=reply)
        else:
            return send_main_menu(user_number)
    except WAUsers.DoesNotExist:
        WAUsers.my_objects.create_user(phone_number=user_number)
        qnumber = WAUsers.my_objects.get(phone_number=user_number)
        add_user_to_cache_DB(phonenumber=user_number, user=qnumber)
        return send_response_messages(msg=reply) 


def add_user_to_cache_DB(phonenumber, user):
    cache.set(phonenumber, user, timeout=EXPIRATION_TIME * 60)
    cache.expire_at(phonenumber, datetime.now() + timedelta(minutes=EXPIRATION_TIME))


def send_response_messages(msg):
    response = MessagingResponse()    
    response.message(msg)
    return HttpResponse(str(response))



def send_main_menu(phone_number):
    options = MainMenu.objects.all()
    username = cache.get(phone_number).user_name
    message = f"Hi, *{username}*, welcome again to Ballot Buddies:\n\n"
    
    for i in options:
        emoji_num = emoji_code_points.get(i.pk)
  
        emoji_char = emoji_num  # handle case where emoji not found
        message += f'{emoji_char}  *{i.feature_en}*\n'

    add_current_action_to_cache_DB(phoneNumber=phone_number, value=MAIN_MENU_ACTION, expire_at=1)
    return send_response_messages(msg=message)

def send_political_parties(phone_number):
    options = Political_Parties.objects.all()
    username = cache.get(phone_number).user_name
    message = f"Hi, *{username}*, Here are the list of parties participating in 2023 harmonised elections.\n\n"
    
    for i in options:
        emoji_num = emoji_code_points.get(i.pk)
  
        emoji_char = emoji_num  # handle case where emoji not found
        message += f'*{i.name}*\n'
    add_current_action_to_cache_DB(phoneNumber=phone_number, value=MAIN_MENU_ACTION, expire_at=1)
    return send_response_messages(msg=message)

def send_presidential_candidates(phone_number):
    options = PresidentialCandidates.objects.all()
    username = cache.get(phone_number).user_name
    message = f"Hi, *{username}*, here are the presidential candidates and their respective political parties participating in the 2023 harmonized elections:\n\n"
    tb1 = pt()
    tb1.max_width = 10
    tb1.field_names=["*CANDIDATE*","*POLITICAL PARTY*"]
    for i in options:
        tb1.add_row([f"{i.name}",f"{i.political_party}"])

    tb1.align["PARTY"] = "l"
    message += tb1.get_string(title = "Presidential Candidates")
    add_current_action_to_cache_DB(phoneNumber=phone_number, value=MAIN_MENU_ACTION, expire_at=1)
    return send_response_messages(msg=message)

def send_mp_start(phone_number):
    username = cache.get(phone_number).user_name
    message = f"Hi, *{username}*, tell us your constituency\ne.g *Chikomba central*"
    add_current_action_to_cache_DB(phoneNumber=phone_number, value=FIND_MP_ACTION, expire_at=1)
    return send_response_messages(msg=message)

def send_mp_end(constituency_name, phone_number):
    username = cache.get(phone_number).user_name
    member_of_parliaments = MemberOfParliamentCandidates.objects.filter(constituency__name__icontains=constituency_name)
    message = f"Hi, *{username}*, here are the MP candidates and their respective political parties participating in the 2023 harmonized elections. In *{constituency_name} constituency*:\n\n"
    tb1 = pt()
    tb1.max_width = 10
    tb1.field_names=["*CANDIDATE*","*POLITICAL PARTY*"]
    for i in member_of_parliaments:
        tb1.add_row([f"{i.name}",f"{i.political_party}"])
    message += tb1.get_string(title = "MP Candidates")
    add_current_action_to_cache_DB(phoneNumber=phone_number, value=MAIN_MENU_ACTION, expire_at=1)
    return send_response_messages(msg=message)

def add_current_action_to_cache_DB(phoneNumber, value, expire_at: int):
    cache.set(f"{CURRENT_ACTION_PREFIX}{phoneNumber}", value, timeout=expire_at * 60)
    cache.expire_at(f"{CURRENT_ACTION_PREFIX}{phoneNumber}", datetime.now() + timedelta(minutes=expire_at))

def invalid_reply():
    _msg = "Invalid response.\n\n To return home reply with *0*"

    return send_response_messages(msg=_msg)