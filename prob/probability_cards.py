# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import math
import numpy as np

def P(num_n, num_r):
    # permutation
    permutation = math.factorial(num_n) / math.factorial(num_n - num_r)
    return permutation


def C(num_n, num_r):
    # combination
    combination = (math.factorial(num_n) / math.factorial(num_n - num_r)) / math.factorial(num_r)
    return combination


def probability(leave_cards):
    prob_dic = {"All": 1}
    prob_dic_list = ["Normal", "Pair", "Flush", "Straight", "Three of a Kind", "Straight Flush", "All"]

    # Straight Flush
    prob_all_flush = P(13, 3) * 4 / P(leave_cards, 3)
    prob_all_straight = math.pow(4, 3) * 11 / P(leave_cards, 3)
    prob_dic["Straight Flush"] = prob_all_flush * prob_all_straight

    # Three of a Kind
    prob_dic["Three of a Kind"] = P(4, 3) * 13 / P(leave_cards, 3)

    # Straight
    prob_dic["Straight"] = math.pow(4, 3) * 11 / P(leave_cards, 3) - prob_dic["Straight Flush"]

    # Flush
    prob_dic["Flush"] = P(13, 3) * 4 / P(leave_cards, 3) - prob_dic["Straight Flush"]

    # Pair
    prob_dic["Pair"] = P(4, 2) * 13 * 50 / P(52, 3) - prob_dic["Three of a Kind"]

    # Normal
    prob_dic["Normal"] = prob_dic["All"] - prob_dic["Pair"] - prob_dic["Flush"] - \
                         prob_dic["Straight"] - prob_dic["Three of a Kind"] - prob_dic["Straight Flush"]

    return prob_dic


def pro_cal():
    prob_dic_list = ["Normal", "Pair", "Flush", "Straight", "Three of a Kind", "Straight Flush", "All"]

    prob_dic_player = probability(52)
    prob_player = np.zeros(7)
    for counter in range(len(prob_dic_list)):
        prob_player[counter] = prob_dic_player[str(prob_dic_list[counter])]

    prob_dic_dealer = probability(49)
    prob_dealer = np.zeros(7)
    for counter in range(len(prob_dic_list)):
        prob_dealer[counter] = prob_dic_dealer[str(prob_dic_list[counter])]
    print(prob_dealer)


if __name__ == '__main__':
    pro_cal()
