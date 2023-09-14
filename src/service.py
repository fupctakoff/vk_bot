from matchers import Matcher
from users_data import USERS_DICT


class Service:
    @classmethod
    def input(cls, user_id, message):
        """Функция обработки входящего сообщения message"""
        # БЛОК ПОГОДЫ
        if message == Matcher.weather + ' сегодня':
            return USERS_DICT[user_id].weather.get_weather('today')
        elif message == Matcher.weather + ' завтра':
            return USERS_DICT[user_id].weather.get_weather('tomorrow')

        # БЛОК ПРОБОК
        elif message == Matcher.traffic_jam:
            return USERS_DICT[user_id].traffic_jam.get_traffic_jam()

        # БЛОК АФИШЫ
        elif message == Matcher.poster + ' сегодня':
            return USERS_DICT[user_id].poster.get_poster('today')
        elif message == Matcher.poster + ' завтра':
            return USERS_DICT[user_id].poster.get_poster('tomorrow')

        # БЛОК ВАЛЮТЫ
        elif message == Matcher.currency:
            return USERS_DICT[user_id].currency.get_currency()

        elif message == "сменить город":
            return input('сюда')
        else:
            return "Пока нет такого функционала"
