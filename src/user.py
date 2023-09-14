from parse_websites.weather_parse import Weather
from parse_websites.traffic_jam_parse import TrafficJam
from parse_websites.poster_parse import Poster
from parse_websites.currency_parse import Currency


class User:
    def __init__(self, city):
        self.city = city
        self.weather = Weather(city=city)
        self.traffic_jam = TrafficJam(city=city)
        self.poster = Poster(city=city)
        self.currency = Currency()

    def change_of_city(self, new_city: str) -> str:
        """Меняет город пользователя"""
        self.city = new_city
        self.weather = Weather(city=self.city)
        self.traffic_jam = TrafficJam(city=self.city)
        self.poster = Poster(city=self.city)
        return self.city
