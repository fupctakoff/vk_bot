import requests
from bs4 import BeautifulSoup

# постоянная переменная для запроса в requests
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


class Currency():
    def __init__(self):
        self.url = 'https://www.banki.ru/products/currency/cb/'

    def get_bs4_from_html(self) -> bool:
        """Парсинг сайта, создание экземпляра класса soup для вывода взятой информации"""
        response = requests.get(url=self.url, headers=HEADER).text
        self.soup = BeautifulSoup(response, 'html.parser')
        return True

    def get_currency(self) -> str:
        """Выводит конечную информацию о курсе валют на сегодня"""
        self.get_bs4_from_html()
        data = self.__parsed_currency_data()

        return f"1USD = {data['usd']}РУБ \n" \
               f"1EUR = {data['eur']}РУБ \n" \
               f"100JPY = {data['jpy']}РУБ \n" \
               f"1GBP = {data['gbp']}РУБ \n" \
               f"1AUD = {data['aud']}РУБ \n"

    def __parsed_currency_data(self) -> dict:
        """Парсит всю информацию с помощью ранее созданного soup объекта"""
        data = {}
        data['usd'] = self.soup.find('tr', {'data-currency-code': 'USD'}).find_all('td')[-2].text
        data['eur'] = self.soup.find('tr', {'data-currency-code': 'EUR'}).find_all('td')[-2].text
        data['jpy'] = self.soup.find('tr', {'data-currency-code': 'JPY'}).find_all('td')[-2].text
        data['gbp'] = self.soup.find('tr', {'data-currency-code': 'GBP'}).find_all('td')[-2].text
        data['aud'] = self.soup.find('tr', {'data-currency-code': 'AUD'}).find_all('td')[-2].text
        return data
