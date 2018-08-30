import app_conf
import requests


def get_coin_list():

    ''' gets the details of all the coins'''
    results = requests.get(app_conf.list_all_coins_api)
    return results.json()


def get_coin_price(coin_symbol, currency_symbol_list):

    '''takes one coin_symbol and a list of currency_symbols'''
    coin_price_params = {
        "fsym": coin_symbol,
        "tsyms": ','.join(currency_symbol_list)
    }

    results = requests.get(app_conf.coin_price_api, coin_price_params)
    return results.json()
