import requests
from bs4 import BeautifulSoup

# постоянная переменная для запроса в requests
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


class Poster():
    def __init__(self, city):
        self.city = city
        self.url1 = f"https://www.afisha.ru/{self.city}/events/na-segodnya/"
        self.url2 = f"https://www.afisha.ru/{self.city}/events/na-zavtra/"

    def get_bs4_from_html(self, day) -> bool:
        """Парсинг сайта, создание экземпляра класса soup для вывода взятой информации"""
        if day == 'today':
            response = requests.get(url=self.url1, headers=HEADER).text
        else:
            response = requests.get(url=self.url2, headers=HEADER).text
        self.soup = BeautifulSoup(response, 'html.parser')
        return True

    def get_poster(self, day: str) -> str:
        """
        Функция - сборщик погоды, формирование конечного ответа
        Вначале парсятся данные сайта вызовом функции get_bs4_from_html()
        """
        self.get_bs4_from_html(day=day)
        data = list(self.__parsed_posters_data())
        return f"Список интересных мероприятий на сегодня: \n\n" \
               f"1. Мероприятие: {data[0][0]}\nКатегория: {data[0][1]} \nСсылка: https://www.afisha.ru/{data[0][2]}\n\n" \
               f"2. Мероприятие: {data[1][0]}\nКатегория: {data[1][1]} \nСсылка: https://www.afisha.ru/{data[1][2]}\n\n" \
               f"3. Мероприятие: {data[2][0]}\nКатегория: {data[2][1]} \nСсылка: https://www.afisha.ru/{data[2][2]}\n\n" \
               f"4. Мероприятие: {data[3][0]}\nКатегория: {data[3][1]} \nСсылка: https://www.afisha.ru/{data[3][2]}\n\n" \
               f"5. Мероприятие: {data[4][0]}\nКатегория: {data[4][1]} \nСсылка: https://www.afisha.ru/{data[4][2]}\n\n"

    def __parsed_posters_data(self):
        """Функция парсинга афиши - выводит генератор со всей взятой информацией"""
        parsed_posters_today = self.soup.find_all('div', {'data-test': 'ITEM'})[:5]
        for i in parsed_posters_today:
            a = i.find('div', {'data-test': 'RESTRICT-TEXT'})
            b = i.find_all('span', {'data-test': 'META-FIELD-VALUE'})[-1]
            c = a.find('a').get('href')
            yield (a.text, b.text, c)
