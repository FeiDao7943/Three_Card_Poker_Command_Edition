# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import sys
import os

sys.path.append(os.path.abspath('.'))
from generate_card import Generator
from combinations import Get_Combinations


def counting_happen():
    game_dic = {"currency": 1000}
    step_1 = Generator(game_dic)
    game_dic = step_1.deal_card(txt=False)

    step_2 = Get_Combinations(game_dic)
    game_dic = step_2.solve_combination()
    # for counter in game_dic:
    #     print(counter, ":", game_dic[counter], end='\n')

    return game_dic


def prob_counter():
    prob = {"Normal": 0, "Pair": 0, "Flush": 0,
            "Straight": 0, "Three_of_a_Kind": 0,
            "Straight_Flush": 0}
    for test_times in range(int(10e20)):
        final_dic = counting_happen()

        prob["Normal"] += final_dic["play_combination_list"][0]
        prob["Pair"] += final_dic["play_combination_list"][1]
        prob["Flush"] += final_dic["play_combination_list"][2]
        prob["Straight"] += final_dic["play_combination_list"][3]
        prob["Three_of_a_Kind"] += final_dic["play_combination_list"][4]
        prob["Straight_Flush"] += final_dic["play_combination_list"][5]

        for counter in (["Normal", "Pair", "Flush", "Straight", "Three_of_a_Kind", "Straight_Flush"]):
            # print("%.6f %%" % float(prob[counter]/(test_times+1)), end=',  ')
            print("%.0f" % float(prob[counter]), end=',  ')

        print("")


if __name__ == '__main__':
    prob_counter()
