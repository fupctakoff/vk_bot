from parse_websites.weather_parse import Weather
from parse_websites.traffic_jam_parse import TrafficJam
from parse_websites.poster_parse import Poster
from parse_websites.currency_parse import Currency
from service import Service
from transliteration.script_transliteration import script_to_translit
from transliteration.transliteration_data import DATA_FOR_POSTER, DATA_FOR_TRAFFIC_JAM


class User:
    def __init__(self, city: str):
        self.city = city
        self.service = Service()
        self.weather = Weather(city=city)
        self.traffic_jam = self.set_traffic_jam(city=city)
        self.poster = self.set_poster(city=city)
        self.currency = Currency()

    def set_traffic_jam(self, city: str) -> TrafficJam:
        if city.lower() in DATA_FOR_TRAFFIC_JAM.keys():
            return TrafficJam(city=DATA_FOR_TRAFFIC_JAM[city.lower()])
        return TrafficJam(script_to_translit(city=city))

    def set_poster(self, city: str) -> Poster:
        if city.lower() in DATA_FOR_POSTER.keys():
            return Poster(city=DATA_FOR_POSTER[city.lower()])
        return Poster(script_to_translit(city=city))

    def change_city(self, new_city: str) -> str:
        """Меняет город пользователя, инвалидирует данных о пользователе"""
        self.city = new_city.lower()
        self.weather = Weather(city=self.city)
        self.traffic_jam = self.set_traffic_jam(city=self.city)
        self.poster = self.set_poster(city=self.city)
        return self.city
