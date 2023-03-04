# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import copy


class Get_Compare:
    def __init__(self, input_dic):
        self.compare_dic = copy.deepcopy(input_dic)
        self.player_win_flag = 0
        self.dealer_win_flag = 0
        self.equal_flag = 0
        self.compare_result_text = ""

    def combinations_compare(self):
        flag_sum_player = 0
        flag_sum_dealer = 0

        for counter in range(len(self.compare_dic["play_combination_list"])):
            flag_sum_player += self.compare_dic["play_combination_list"][counter]
            flag_sum_dealer += self.compare_dic["deal_combination_list"][counter]
        # print(flag_sum_player)
        # print(flag_sum_player)

        # No Double Combinations
        if (flag_sum_player + flag_sum_player) == 2:
            for counter in range(len(self.compare_dic["play_combination_list"])):
                counter = 6 - 1 - counter
                flag_gap = self.compare_dic["play_combination_list"][counter] - \
                           self.compare_dic["deal_combination_list"][counter]
                flag_sum = self.compare_dic["play_combination_list"][counter] + \
                           self.compare_dic["deal_combination_list"][counter]

                if flag_sum == 1:
                    if self.compare_dic["play_combination_list"][counter]:
                        self.player_win_flag = 1
                        # print("Player's Cards Are '%s', Win!" % (self.compare_dic["combination_list"][counter]))
                        self.compare_result_text = ("Player's Cards Are '%s', Win!" %
                                                    (self.compare_dic["combination_list"][counter]))
                        break

                    if self.compare_dic["deal_combination_list"][counter]:
                        self.dealer_win_flag = 1
                        # print("Dealer's Cards Are '%s', Win!" % (self.compare_dic["combination_list"][counter]))
                        self.compare_result_text = ("Dealer's Cards Are '%s', Win!" %
                                                    (self.compare_dic["combination_list"][counter]))
                        break

                if flag_sum == 2:
                    # Not Both Pair
                    if True:
                        # Compare Second Larger Card
                        player_score_1st = int(self.compare_dic["player_read_value"][2][1])
                        dealer_score_1st = int(self.compare_dic["dealer_read_value"][2][1])
                        # print(player_score_1st)
                        # print(dealer_score_1st)
                        if player_score_1st > dealer_score_1st:
                            self.player_win_flag = 1
                            # print("Player's Cards Are '%s' And Larger, Win!" % (
                            #     self.compare_dic["combination_list"][counter]))
                            self.compare_result_text = ("Player's Cards Are '%s' And Larger in First, Win!" %
                                                        (self.compare_dic["combination_list"][counter]))
                            break
                        if player_score_1st < dealer_score_1st:
                            self.dealer_win_flag = 1
                            # print("Dealer's Cards Are '%s' And Larger, Win!" %
                            #       (self.compare_dic["combination_list"][counter]))
                            self.compare_result_text = ("Dealer's Cards Are '%s' And Larger in First, Win!" %
                                                        (self.compare_dic["combination_list"][counter]))
                            break

                        # The Largest is Same, Compare Second Larger Card
                        if player_score_1st == dealer_score_1st:
                            player_score_2nd = int(self.compare_dic["player_read_value"][1][1])
                            dealer_score_2nd = int(self.compare_dic["dealer_read_value"][1][1])
                            # print(player_score_2nd)
                            # print(dealer_score_2nd)
                            if player_score_2nd > dealer_score_2nd:
                                self.player_win_flag = 1
                                # print("Player's Cards Are '%s' And Larger, Win!" % (
                                #     self.compare_dic["combination_list"][counter]))
                                self.compare_result_text = ("Player's Cards Are '%s' And Larger in Second, Win!" %
                                                            (self.compare_dic["combination_list"][counter]))
                                break
                            if player_score_2nd < dealer_score_2nd:
                                self.dealer_win_flag = 1
                                # print("Dealer's Cards Are '%s' And Larger, Win!" % (
                                #     self.compare_dic["combination_list"][counter]))
                                self.compare_result_text = ("Dealer's Cards Are '%s' And Larger in Second, Win!" %
                                                            (self.compare_dic["combination_list"][counter]))
                                break

                            # The Second Largest is Same, Compare Third Larger Card
                            if player_score_2nd == dealer_score_2nd:
                                player_score_3rd = int(self.compare_dic["player_read_value"][0][1])
                                dealer_score_3rd = int(self.compare_dic["dealer_read_value"][0][1])
                                # print(player_score_3rd)
                                # print(dealer_score_3rd)
                                if player_score_3rd > dealer_score_3rd:
                                    self.player_win_flag = 1
                                    # print("Player's Cards Are '%s' And Larger, Win!" % (
                                    #     self.compare_dic["combination_list"][counter]))
                                    self.compare_result_text = ("Player's Cards Are '%s' And Larger in Third, Win!" %
                                                                (self.compare_dic["combination_list"][counter]))
                                    break
                                if player_score_3rd < dealer_score_3rd:
                                    self.dealer_win_flag = 1
                                    # print("Dealer's Cards Are '%s' And Larger, Win!" % (
                                    #     self.compare_dic["combination_list"][counter]))
                                    self.compare_result_text = ("Dealer's Cards Are '%s' And Larger in Third, Win!" %
                                                                (self.compare_dic["combination_list"][counter]))
                                    break
                                if player_score_3rd == dealer_score_3rd:
                                    self.equal_flag = 1
                                    self.compare_result_text = "Card's Are Equal!"

    def solve_compare(self):
        self.combinations_compare()
        self.compare_dic["player_win_flag"] = self.player_win_flag
        self.compare_dic["dealer_win_flag"] = self.dealer_win_flag
        self.compare_dic["equal_flag"] = self.equal_flag
        self.compare_dic["compare_result_text"] = self.compare_result_text
        print(self.compare_result_text)
        return self.compare_dic



if __name__ == '__main__':
    game_dic = {"currency": 1000}
    game_dic["player_read_value"] = [['Heart', '3'], ['Club', '4'], ['Heart', '5']]
    game_dic["dealer_read_value"] = [['Spade', '3'], ['Diamond', '4'], ['Club', '5']]
    game_dic["play_combination_list"] = [0, 0, 0, 1, 0, 0]
    game_dic["deal_combination_list"] = [0, 0, 0, 1, 0, 0]
    game_dic["combination_list"] = ['Normal', 'Pair', 'Flush', 'Straight', 'Three of a Kind', 'Straight Flush']
    test = Get_Compare(game_dic)
    game_dic = test.solve_compare()
    for counter in game_dic:
        print(counter, ":", game_dic[counter], end='\n')
