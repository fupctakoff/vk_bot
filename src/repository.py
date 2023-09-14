from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from service import Service
from config import TOKEN, GROUP_ID
from users_data import USERS_DICT
from user import User
from keyboards.main_kb import main_keyboard

class Bot():
    group_id = GROUP_ID

    def __init__(self, token=TOKEN):
        self.vk_session = VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=self.group_id)
        self.vk = self.vk_session.get_api()

    def send_message(self, user_id, message, keyboard=main_keyboard):
        """Механизм ответа пользователю"""
        self.vk.messages.send(user_id=user_id, message=message, random_id=0, keyboard=main_keyboard.get_keyboard())

    def get_user_city(self, user_id):
        """Получение текущего города пользователя"""
        #return self.vk.users.get(user_id=user_id, fields=('city',))[0]['city']['title'].lower()
        return 'kazan'

    def start(self):
        """Функция, которая ждет события, и вызывает остальной функционал для ответного сообщения"""
        for event in self.longpoll.listen():
            print(event)
            if event.object['message']['from_id'] not in USERS_DICT.keys():
                USERS_DICT[event.object['message']['from_id']] = User(city=self.get_user_city(
                    user_id=event.object['message']['from_id']))

            if event.type == VkBotEventType.MESSAGE_NEW:

                self.send_message(user_id=event.object['message']['from_id'],
                                  message=Service.input(user_id=event.object['message']['from_id'],
                                                        message=event.object['message']['text']))



bob = Bot()
bob.start()
