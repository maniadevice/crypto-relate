import app_conf
import math


class Coin:

    base_url = app_conf.crypto_compare_base_url

    def __init__(self, id, coin_name, coin_symbol, image_url):

        self.id = id
        self.coin_name = coin_name
        self.coin_symbol = coin_symbol
        self.image_url = self.base_url + image_url

    @staticmethod
    def get_exponent_factor(price):

        # price = float(price)
        if (price > 1.0):
            return 0

        return math.floor(math.log(1 / price, 10))


class CoinRelate:

    def __init__(self, first_coin, second_coin, relative_price):

        self.first_coin = first_coin
        self.second_coin = second_coin
        self.relative_price = relative_price
