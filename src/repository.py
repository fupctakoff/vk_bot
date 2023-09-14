from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from config import TOKEN, GROUP_ID
from users_data import USERS_DICT
from user import User
from keyboards.main_kb import main_keyboard
from keyboards.today_tomorrow_kb import support_keyboard
from matchers import Matcher


class Bot():
    group_id = GROUP_ID

    def __init__(self, token=TOKEN):
        self.vk_session = VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=self.group_id)
        self.vk = self.vk_session.get_api()

    def send_message(self, user_id, message, keyboard=main_keyboard):
        """Механизм ответа пользователю"""
        self.vk.messages.send(user_id=user_id, message=message, random_id=0, keyboard=keyboard.get_keyboard())

    def get_user_city(self, user_id):
        """Получение текущего города пользователя"""
        try:
            current_city_from_profile = self.vk.users.get(user_id=user_id, fields=('city',))[0]['city']['title'].lower()
            return current_city_from_profile
        except KeyError:
            return 'Москва'

    def start(self):
        """Функция, которая ждет события, и вызывает остальной функционал для ответного сообщения"""
        for event in self.longpoll.listen():
            print(event)
            id = event.object['message']['from_id']
            msg = event.object['message']['text']

            # Проверка на пользователя в списке
            if event.object['message']['from_id'] not in USERS_DICT.keys():
                USERS_DICT[id] = User(city=self.get_user_city(user_id=id))
            # проверка, не сменил ли существующий пользователь город в профиле
            else:
                if USERS_DICT[id].city != self.get_user_city(id):
                    USERS_DICT[id].change_city(self.get_user_city(user_id=id))

            # обработка нового сообщения
            if event.type == VkBotEventType.MESSAGE_NEW:
                if msg == 'Начать':
                    response = USERS_DICT[id].service.input(user_id=id, message=msg)
                    self.send_message(user_id=id, message=response)
                # Если пользователь вошел во вложенный блок (погода или афиша) - устанавливается маркер для клавиш "сегодня", "завтра"
                elif msg in [Matcher.weather, Matcher.poster]:
                    response = USERS_DICT[id].service.input(user_id=id, message=msg)
                    USERS_DICT[id].service.mark = msg
                    self.send_message(user_id=id, message=response, keyboard=support_keyboard)
                # Обработка всех остальных сообщений
                else:
                    response = USERS_DICT[id].service.input(user_id=id, message=msg)
                    self.send_message(user_id=id, message=response)
