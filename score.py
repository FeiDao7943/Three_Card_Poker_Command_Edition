# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import copy


def limit_input(limit, value_name):
    pass_flag_1 = 0
    while not pass_flag_1:
        try:
            locals()[value_name] = int(input("Input the %s: " % value_name))
            if locals()[value_name] <= limit:
                pass_flag_1 = 1
            if locals()[value_name] > limit:
                print("Value of %s is over the limit." % value_name)
        except:
            print("Enter integral number.")
    return locals()[value_name]


class Get_Score:
    def __init__(self, input_dic):
        self.score_dic = copy.deepcopy(input_dic)
        self.ante = 0
        self.pair_plus = 0
        self.play = 0
        self.pay_play_flag = 0

    def get_input_1(self):
        ante = limit_input(self.score_dic["currency"] / 2, "ante")
        self.score_dic["currency"] -= ante
        to_print = ("[Currency - %d: %d]" % (ante, self.score_dic["currency"]))
        print("\033[1;31m%s\033[0m" % to_print)

        pair_plus = limit_input(self.score_dic["currency"] - ante, "pair_plus")
        self.score_dic["currency"] -= pair_plus
        to_print = ("[Currency - %d: %d]" % (pair_plus, self.score_dic["currency"]))
        print("\033[1;31m%s\033[0m" % to_print)

        # print(ante)
        # print(pair_plus)
        self.ante = ante
        self.pair_plus = pair_plus

    def get_input_2(self):
        pass_flag_2 = 0
        while not pass_flag_2:
            try:
                self.pay_play_flag = input("Pay play or not?[y/n]: ")
                if self.pay_play_flag == "y":
                    self.play = self.ante
                    self.score_dic["currency"] -= self.play
                    to_print = ("[Currency - %d: %d]" % (self.play, self.score_dic["currency"]))
                    print("\033[1;31m%s\033[0m" % to_print)
                    pass_flag_2 = 1
                if self.pay_play_flag == "n":
                    self.play = 0
                    to_print = ("[Currency - %d: %d]" % (self.play, self.score_dic["currency"]))
                    print("\033[1;31m%s\033[0m" % to_print)
                    pass_flag_2 = 1
                if (self.pay_play_flag != "y") and (self.pay_play_flag != "n"):
                    print("Error input.")
            except:
                print("Error input.")

    def solve_score(self):
        print("----------------------------%s----------------------------" % \
              ("ROUND" + str(self.score_dic["round_num"])))

        earn = 0
        print("[Currency: %d]" % self.score_dic["currency"])
        self.get_input_1()
        print("\nPlayer: ", self.score_dic["player_card"])
        self.get_input_2()
        print("Dealer: ", self.score_dic["dealer_card"])

        # Dealer Win or Equal
        if self.score_dic["dealer_win_flag"] or self.score_dic["equal_flag"]:
            to_print = (self.score_dic["compare_result_text"])
            print("\033[1;31m%s\033[0m" % to_print)
            # Player's card is Straight
            if self.score_dic["play_combination_list"][3]:
                earn += self.pair_plus
                earn += self.ante * 1
                earn += self.pair_plus * 6

            # Player's card is Three of a Kind
            if self.score_dic["play_combination_list"][4]:
                earn += self.pair_plus
                earn += self.ante * 4
                earn += self.pair_plus * 30

            # Player's card is Straight Flush
            if self.score_dic["play_combination_list"][5]:
                earn += self.pair_plus
                earn += self.ante * 5
                earn += self.pair_plus * 40

        # Player Win
        if self.score_dic["player_win_flag"]:
            to_print = (self.score_dic["compare_result_text"])
            print("\033[1;31m%s\033[0m" % to_print)

            # Player's card is Normal
            if self.score_dic["play_combination_list"][0]:
                # Dealer's card higher than Q high
                if int(self.score_dic["dealer_read_value"][2][1]) >= 12:
                    earn += self.ante + self.play
                    earn += (self.ante + self.play) * 1
                if int(self.score_dic["dealer_read_value"][2][1]) <= 12:
                    earn += self.play
                    earn += (self.ante + self.play) * 1

            # Player's card is Pair
            if self.score_dic["play_combination_list"][1]:
                earn += self.ante + self.pair_plus + self.play
                earn += (self.ante + self.play) * 1
                earn += self.pair_plus * 1

            # Player's card is Flush
            if self.score_dic["play_combination_list"][2]:
                earn += self.ante + self.pair_plus + self.play
                earn += (self.ante + self.play) * 1
                earn += self.pair_plus * 3

            # Player's card is Straight
            if self.score_dic["play_combination_list"][3]:
                earn += self.ante + self.pair_plus + self.play
                earn += (self.ante + self.play) * 1
                earn += self.pair_plus * 6

            # Player's card is Three of a Kind
            if self.score_dic["play_combination_list"][4]:
                earn += self.ante + self.pair_plus + self.play
                earn += (self.ante + self.play) * 4
                earn += self.pair_plus * 30

            # Player's card is Straight Flush
            if self.score_dic["play_combination_list"][5]:
                earn += self.ante + self.pair_plus + self.play
                earn += (self.ante + self.play) * 5
                earn += self.pair_plus * 40

        self.score_dic["currency"] += earn
        to_print = ("[Currency + %d: %d]" % (earn, self.score_dic["currency"]))
        print("\033[1;36m%s\033[0m" % to_print)
        input("---------------------Press Enter to Next---------------------\n")
        return self.score_dic


if __name__ == '__main__':
    game_dic = {"currency": 1000}
    game_dic["player_card"] = ['Club_4', 'Diamond_6', 'Club_5']
    game_dic["dealer_card"] = ['Club_K', 'Heart_Q', 'Heart_Q']
    game_dic["player_read_value"] = [['Club', '4'], ['Club', '5'], ['Diamond', '6']]
    game_dic["dealer_read_value"] = [['Heart', '12'], ['Heart', '12'], ['Club', '13']]
    game_dic["player_win_flag"] = 0
    game_dic["dealer_win_flag"] = 1
    game_dic["equal_flag"] = 0
    game_dic["compare_result_text"] = "Dealer's Cards Are 'Pair' And Larger in Second, Win!"
    game_dic["play_combination_list"] = [0, 0, 0, 1, 0, 0]
    game_dic["deal_combination_list"] = [0, 0, 0, 1, 0, 0]
    game_dic["combination_list"] = ['Normal', 'Pair', 'Flush', 'Straight', 'Three of a Kind', 'Straight Flush']
    test = Get_Score(game_dic)
    game_dic = test.solve_score()
    for counter_test in game_dic:
        print(counter_test, ":", game_dic[counter_test], end='\n')
