import api_request

coin_data = api_request.get_coin_list()


def get_relative_price(outgoing_coins_list, incoming_coins_list):

    for coin_symbol in outgoing_coins_list:

        relative_prices = api_request.get_coin_price(
            coin_symbol, incoming_coins_list)

        print("###############")
        print(coin_data["Data"][coin_symbol]["FullName"])
        print("###############")
        for symbol in relative_prices:

            # second coin bigger
            if (float(relative_prices[symbol]) < 1.0):
                first_coin_count = 1 / float(relative_prices[symbol])
                second_coin_count = 1
            else:
                first_coin_count = 1
                second_coin_count = float(relative_prices[symbol])

            print("{} {} = {} {}".format(
                str(first_coin_count),
                coin_data["Data"][coin_symbol]["FullName"],
                str(second_coin_count),
                coin_data["Data"][symbol]["FullName"]
            ))

        print("\n\n")


def main():

    outgoing_coins_list = input("Enter coin symbols of coins you want to exchange, separated by commas: \n").strip('\t\n\r').replace(" ", "").upper().split(',')
    incoming_coins_list = input("Enter coin symbols of coins you want to get, separated by commas:\n").strip('\t\n\r').replace(" ", "").upper().split(',')

    get_relative_price(outgoing_coins_list, incoming_coins_list)


main()
