import requests
from bs4 import BeautifulSoup

# постоянная переменная для запроса в requests
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


class Weather:
    def __init__(self, city):
        self.city = city
        self.url = f'https://sinoptik.ua/погода-{self.city}'

    def get_bs4_from_html(self) -> bool:
        """Парсинг сайта, создание экземпляра класса soup для вывода взятой информации"""
        response = requests.get(url=self.url, headers=HEADER).text
        self.soup = BeautifulSoup(response, 'html.parser')
        return True

    def get_weather(self, day) -> str:
        """
        Функция - сборщик погоды, формирование конечного ответа
        Вначале парсятся данные сайта вызовом функции get_bs4_from_html()
        """
        self.get_bs4_from_html()
        min = self.__get_min_and_max_weather_by_day(condition='min', day=day)
        max = self.__get_min_and_max_weather_by_day(condition='max', day=day)
        return f"Минимальная температура в городе {self.city} составляет {min}, максимальная {max}"

    def __get_min_and_max_weather_by_day(self, condition: str, day: str) -> str:
        """
        Парсинг числа градусов
        condition: 'min' | 'max' - какое число парсить, минимальное или максимальное
        day: 'today' | 'tomorrow' - в какой день интересна погода, сегодня или завтра
        """
        if day == 'today':
            return self.soup.find('div', {'class': condition}).find('span').text
        elif day == 'tomorrow':
            return self.soup.find_all('div', {'class': condition})[1].find('span').text
        else:
            return 'Погода в указанный день не найдена'
