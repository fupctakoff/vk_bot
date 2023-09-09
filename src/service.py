from matchers import Matcher

class Service:
    @classmethod
    def input(cls, message):
        """Функция обработки входящего сообщения message"""
        if message == Matcher.weather:
            return "Функция парсинга погоды" #Тут возможно разветвление на сегодня/завтра - зависит от функционала парсинга
        elif message == Matcher.traffic_jam:
            return "Функция парсинга пробок"
        elif message == Matcher.poster:
            return "Функция парсинга афишы"
        elif message == Matcher.currency:
            return "Функция парсинга валюты"
        elif message == "сменить город":
            return "Функция смена города"
        else:
            return "Пока нет такого функционала"
