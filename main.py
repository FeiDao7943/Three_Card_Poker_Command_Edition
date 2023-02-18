# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
from generate_card import Generator
from referee import Referee_method

def main():
    currency = 1000
    round_count = 0
    while currency > 0:
        round_count += 1
        input("Press Enter to Next Round!")
        print("\n")
        print("----------------Round "+str(round_count)+" ------------------")
        get_card = Generator()
        player_card, dealer_card = get_card.deal_card()
        print("Begin Currency: ", currency)
        test = Referee_method(player_card, dealer_card)
        currency = test.final(currency)
        print("Final Currency: ", currency)
        print("------------------------------------------")

    print("\n")
    print("------------------------------------------")
    print("\033[1;31m                 Game over\033[0m")
    print("------------------------------------------")


if __name__ == '__main__':
    main()

    # print('\033[1;31m欢迎使用学生选课系统\033[0m')
