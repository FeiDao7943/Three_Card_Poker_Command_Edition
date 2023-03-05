# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import os
from generate_card import Generator
from combinations import Get_Combinations
from compare import Get_Compare
from score import Get_Score

os.system('')


def main():
    game_dic = {"currency": 1000, "round_num": 0}
    while game_dic["currency"] > 0:
        game_dic["round_num"] += 1

        # Step 1, Generate the Cards
        step_1 = Generator(game_dic)
        game_dic = step_1.deal_card(txt=False)

        # Step 2, Cognition of Combinations
        step_2 = Get_Combinations(game_dic)
        game_dic = step_2.solve_combination()

        # Step 3, Compare The Cards
        step_3 = Get_Compare(game_dic)
        game_dic = step_3.solve_compare()

        # Step 4, Player Input
        step_4 = Get_Score(game_dic)
        game_dic = step_4.solve_score()
        # for counter_test in game_dic:
        #     print(counter_test, ":", game_dic[counter_test], end='\n')

    print("\nGame Over!\n")


if __name__ == '__main__':
    main()
