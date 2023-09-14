import requests

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


class TrafficJam():
    def __init__(self, city):
        self.city = city
        self.url = f'https://jam.api.2gis.com/{self.city}/meta/score/0/'

    def get_traffic_jam(self):
        """
        Функция парсинга цифры состояния пробок в городе user_city.
        Поступает GET-запрос напрямую к скрипту выведения состояния пробок в 2gis
        """
        result = requests.get(url=self.url, headers=HEADER)
        if result.status_code == 404:
            return 'Информация о пробках не была найдена, перепроверьте правильность названия города'
        else:
            return f"В вашем городе пробки {int(result.text[1])} баллов"
