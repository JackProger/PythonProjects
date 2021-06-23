from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import COVID19Py
import requests

token = "48ba954171b8952ad3b1743d6b00b56af76dc8d0f1511d023a19f534dac07dbdbcfe0f50a3cf9753b208b"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

covid19 = COVID19Py.COVID19()
anekt = ('Одним прекрасным вечером плавают два гея в дорогущем бассейне, решили устроить себе романтик - свечи все дела.'
         'Один из них смотрит - сперма плавает на поверхности и спрашивает у второго: "Дорогой, ты кончил?", а тот ему отвечает: "Нет, пернул".')
def cor():
    location = covid19.getLocationByCountryCode("RU")
    
    vk_session.method('messages.send', {'user_id': event.user_id, 'message': f"Подтверждено: {location[0]['latest']['confirmed']}\nУмерших: {location[0]['latest']['deaths']}\n", 'random_id': 0})
def ver():
    x = random.randint(0,100)
    vk_session.method('messages.send', {'user_id': event.user_id, 'message': f'{x}%', 'random_id': 0})
   


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, я бот Евгений, если хочешь узнать больше напиши "что ты умеешь?"', 'random_id': 0})
            elif response == "что ты умеешь?":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вот список команд: "расскажи анекдот", "ава", "коронавирус", "вероятность...".', 'random_id': 0})
            elif response == "расскажи анекдот":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': anekt, 'random_id': 0})
            elif response == "ава": 
               vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Держи, если не нравится напиши другая", "attachment": "photo-100750597_457262684%2Falbum-100750597_00%2Frev", "random_id": 0}) 
            
            elif response == "другая":
               vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Держи, опять не доволен? Напиши ещё авы.", "attachment": "photo-100750597_457262633%2Falbum-100750597_00%2Frev", "random_id": 0})
            elif response == "ещё авы":
               vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Ты задолбал! Хватит!", "attachment": "photo-100750597_457262584%2Falbum-100750597_00%2Frev", "random_id": 0})
            elif "вероятность" in response:
               ver()   
            elif response == "коронавирус":
                cor()
                
            else:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Сори, но я не знаю что это((", 'random_id': 0})
            
            



