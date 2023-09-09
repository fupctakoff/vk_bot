from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from service import Service
from config import TOKEN, GROUP_ID


class Bot():
    group_id = GROUP_ID

    def __init__(self, token=TOKEN):
        self.vk_session = VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=self.group_id)
        self.vk = self.vk_session.get_api()

    def send_message(self, user_id, message):
        """Механизм ответа пользователю"""
        self.vk.messages.send(user_id=user_id, message=message, random_id=0)

    def get_user_city(self, user_id):
        """Получение текущего города пользователя"""
        return self.vk.users.get(user_id=user_id, fields=('city',))[0]['city']['title']

    def start(self):
        """Функция, которая ждет события"""
        for event in self.longpoll.listen():
            # тестовый вывод - потом убрать
            print(event, 1)
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.send_message(user_id=event.object['message']['from_id'],
                                  message=Service.input(event.object['message']['text']))
            # тестовый вывод города - потом убрать
            print(self.get_user_city(event.object['message']['from_id']))


bob = Bot()
bob.start()
