from classdeomo.coin import Coin

def main():
    my_coin = Coin('Flower')
    print(my_coin.get_side())
    my_coin.toss()
    print(my_coin.get_side())
main()