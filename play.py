# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
from generate_card import Generator
from combinations import Get_Combinations


def main():
    game_dic = {"currency": 1000}
    step_1 = Generator(game_dic)
    game_dic = step_1.deal_card(txt=False)

    step_2 = Get_Combinations(game_dic)
    game_dic = step_2.solve_combination()
    for counter in game_dic:
        print(counter, ":", game_dic[counter], end='\n')


if __name__ == '__main__':
    main()
