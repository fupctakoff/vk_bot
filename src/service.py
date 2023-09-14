from matchers import Matcher
from users_data import USERS_DICT


class Service:
    mark = None

    def set_default_mark(self):
        self.mark = None

    def input(self, user_id, message) -> str:
        """Обработка входящего сообщения message"""
        match message:

            # БЛОК ПРОБОК
            case Matcher.traffic_jam:
                return USERS_DICT[user_id].traffic_jam.get_traffic_jam()

            # БЛОК ВАЛЮТЫ
            case Matcher.currency:
                return USERS_DICT[user_id].currency.get_currency()

            # БЛОК СЕГОДНЯ ДЛЯ ПОГОДЫ И АФИШЫ
            case 'сегодня':
                if self.mark == Matcher.weather:
                    self.set_default_mark()
                    return USERS_DICT[user_id].weather.get_weather('today')
                if self.mark == Matcher.poster:
                    self.set_default_mark()
                    return USERS_DICT[user_id].poster.get_poster('today')
                return 'Сначала выберите, что вы хотите узнать про сегодня: состояние погоды или афишу'

            # БЛОК ЗАВТРА ДЛЯ ПОГОДЫ И АФИШЫ
            case 'завтра':
                if self.mark == Matcher.weather:
                    self.set_default_mark()
                    return USERS_DICT[user_id].weather.get_weather('tomorrow')
                if self.mark == Matcher.poster:
                    self.set_default_mark()
                    return USERS_DICT[user_id].poster.get_poster('tomorrow')
                return 'Сначала выберите, что вы хотите узнать про завтра: состояние погоды или афишу'

            # БЛОК НАЖАТИЕ НА КНОПКУ ПОГОДА ИЛИ АФИША
            case Matcher.weather | Matcher.poster:
                return 'В какой день?'

            # БЛОК НАЗАД
            case 'назад':
                return 'Возвращаемся'

            # БЛОК СМЕНИТЬ ГОРОД
            case 'сменить город':
                return 'Введите название вашего города в следующем сообщении'

            # БЛОК СТАРТА
            case 'Начать':
                return 'Вас приветствует бот Боб. \n Он может показывать афишу, валюту, балл пробки.\n\n \
                Если в вашем профиле нет города, вся информация в данном боте будет отображаться для г.Москва.\n \
                            Вы можете указать/поменять город в профиле, или воспользоваться кнопкой "Сменить город"'

            # БЛОК ВСЕ ОСТАЛЬНОЕ
            case _:
                if self.mark == 'сменить город':
                    self.set_default_mark()
                    USERS_DICT[user_id].change_city(new_city=message)
                    return 'Город успешно изменен'
                return "Пока нет такого функционала"
