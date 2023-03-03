# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import copy


class Get_Combinations:
    def __init__(self, input_dic):
        self.combination_dic = copy.deepcopy(input_dic)
        self.player_card = copy.deepcopy(self.combination_dic["player_card"])
        self.dealer_card = copy.deepcopy(self.combination_dic["dealer_card"])
        self.player_read = []
        self.dealer_read = []
        self.combinations = ["Normal", "Pair", "Flush", "Straight", "Three of a Kind", "Straight Flush"]

        self.existing_flag_dic = {"Normal_flag": 1, "Pair_flag": 0, "Flush_flag": 0,
                                  "Straight_flag": 0, "Three_of_a_Kind_flag": 0,
                                  "Straight_Flush_flag": 0}
        self.player_combinations_dic = None
        self.dealer_combinations_dic = None
        self.player_read_value = None
        self.dealer_read_value = None

    def read_card(self):
        for counter in range(len(self.player_card)):
            self.player_read.append(self.player_card[counter].split("_", 2))
            self.dealer_read.append(self.dealer_card[counter].split("_", 2))

        self.player_read = self.ordering(self.player_read)
        self.dealer_read = self.ordering(self.dealer_read)
        # print(self.player_read)  # 3*2
        # print(self.dealer_read)  # 3*2

    def ordering(self, read_cards):
        min_1st = 0
        min_2nd = 0
        min_3rd = 0
        read_cards_copy = copy.deepcopy(read_cards)

        for counter in range(3):
            if read_cards_copy[counter][1] == "J":
                read_cards_copy[counter][1] = "11"
            if read_cards_copy[counter][1] == "Q":
                read_cards_copy[counter][1] = "12"
            if read_cards_copy[counter][1] == "K":
                read_cards_copy[counter][1] = "13"
            if read_cards_copy[counter][1] == "A":
                read_cards_copy[counter][1] = "14"

        if int(read_cards_copy[0][1]) <= int(read_cards_copy[1][1]):
            min_1st = 0
            min_2nd = 1
            if int(read_cards_copy[1][1]) <= int(read_cards_copy[2][1]):
                min_3rd = 2
            if int(read_cards_copy[1][1]) >= int(read_cards_copy[2][1]):
                min_3rd = 1
                if int(read_cards_copy[0][1]) <= int(read_cards_copy[2][1]):
                    min_2nd = 2
                if int(read_cards_copy[0][1]) >= int(read_cards_copy[2][1]):
                    min_1st = 2
                    min_2nd = 0

        if int(read_cards_copy[0][1]) >= int(read_cards_copy[1][1]):
            min_1st = 1
            min_2nd = 0
            if int(read_cards_copy[2][1]) >= int(read_cards_copy[0][1]):
                min_3rd = 2
            if int(read_cards_copy[2][1]) <= int(read_cards_copy[0][1]):
                min_3rd = 0
                if int(read_cards_copy[2][1]) >= int(read_cards_copy[1][1]):
                    min_2nd = 2
                if int(read_cards_copy[2][1]) <= int(read_cards_copy[1][1]):
                    min_1st = 2
                    min_2nd = 1

        new_order = [[read_cards[min_1st][0], read_cards[min_1st][1]],
                     [read_cards[min_2nd][0], read_cards[min_2nd][1]],
                     [read_cards[min_3rd][0], read_cards[min_3rd][1]]]
        # print(new_order)
        return new_order

    def reset_exiting_flag(self):
        self.existing_flag_dic["Normal_flag"] = 1
        self.existing_flag_dic["Pair_flag"] = 0
        self.existing_flag_dic["Flush_flag"] = 0
        self.existing_flag_dic["Straight_flag"] = 0
        self.existing_flag_dic["Three_of_a_Kind_flag"] = 0
        self.existing_flag_dic["Straight_Flush_flag"] = 0

    def Straight_Flush_judgement(self, read_cards):
        Flush_flag = 0
        Straight_flag = 0

        read_cards_copy = copy.deepcopy(read_cards)

        for counter in range(3):
            if read_cards_copy[counter][1] == "J":
                read_cards_copy[counter][1] = "11"
            if read_cards_copy[counter][1] == "Q":
                read_cards_copy[counter][1] = "12"
            if read_cards_copy[counter][1] == "K":
                read_cards_copy[counter][1] = "13"
            if read_cards_copy[counter][1] == "A":
                read_cards_copy[counter][1] = "14"

        if read_cards_copy[0][0] == read_cards_copy[1][0]:
            if read_cards_copy[1][0] == read_cards_copy[2][0]:
                Flush_flag = 1

        if int(read_cards_copy[0][1]) == int(read_cards_copy[1][1]) - 1:
            if int(read_cards_copy[1][1]) == int(read_cards_copy[2][1]) - 1:
                Straight_flag = 1

        if Flush_flag and Straight_flag:
            self.existing_flag_dic["Normal_flag"] = 0
            self.existing_flag_dic["Straight_Flush_flag"] = 1
            # print("Straight_Flush_flag")

    def Three_of_a_Kind_judgement(self, read_cards):
        if read_cards[0][1] == read_cards[1][1]:
            if read_cards[1][1] == read_cards[2][1]:
                self.existing_flag_dic["Normal_flag"] = 0
                self.existing_flag_dic["Three_of_a_Kind_flag"] = 1
                # print("Three_of_a_Kind_flag")

    def Straight_judgement(self, read_cards):
        read_cards_copy = copy.deepcopy(read_cards)

        for counter in range(3):
            if read_cards_copy[counter][1] == "J":
                read_cards_copy[counter][1] = "11"
            if read_cards_copy[counter][1] == "Q":
                read_cards_copy[counter][1] = "12"
            if read_cards_copy[counter][1] == "K":
                read_cards_copy[counter][1] = "13"
            if read_cards_copy[counter][1] == "A":
                read_cards_copy[counter][1] = "14"

        if int(read_cards_copy[0][1]) == int(read_cards_copy[1][1]) - 1:
            if int(read_cards_copy[1][1]) == int(read_cards_copy[2][1]) - 1:
                self.existing_flag_dic["Normal_flag"] = 0
                if not self.existing_flag_dic["Straight_Flush_flag"]:
                    self.existing_flag_dic["Straight_flag"] = 1
                # print("Straight_flag")

    def Flush_judgement(self, read_cards):
        if read_cards[0][0] == read_cards[1][0]:
            if read_cards[1][0] == read_cards[2][0]:
                self.existing_flag_dic["Normal_flag"] = 0
                if not self.existing_flag_dic["Straight_Flush_flag"]:
                    self.existing_flag_dic["Flush_flag"] = 1
                # print("Flush_flag")

    def Pair_judgement(self, read_cards):
        if (read_cards[0][1] == read_cards[1][1]) or \
                (read_cards[1][1] == read_cards[2][1]) or \
                (read_cards[0][1] == read_cards[2][1]):
            self.existing_flag_dic["Normal_flag"] = 0
            if not self.existing_flag_dic["Three_of_a_Kind_flag"]:
                self.existing_flag_dic["Pair_flag"] = 1
            # print("Flush_flag")

    def combination_cognition(self, input_card):
        self.reset_exiting_flag()
        self.Straight_Flush_judgement(input_card)
        self.Three_of_a_Kind_judgement(input_card)
        self.Straight_judgement(input_card)
        self.Flush_judgement(input_card)
        self.Pair_judgement(input_card)
        # for counter in self.existing_flag_dic:
        #     print(counter, ":", self.existing_flag_dic[counter], end='\n')
        # print("")
        return self.existing_flag_dic

    def read_value(self, read_cards):
        read_cards_copy = copy.deepcopy(read_cards)
        for counter in range(3):
            if read_cards_copy[counter][1] == "J":
                read_cards_copy[counter][1] = "11"
            if read_cards_copy[counter][1] == "Q":
                read_cards_copy[counter][1] = "12"
            if read_cards_copy[counter][1] == "K":
                read_cards_copy[counter][1] = "13"
            if read_cards_copy[counter][1] == "A":
                read_cards_copy[counter][1] = "14"
        return read_cards_copy

    def solve_combination(self):
        self.read_card()

        tem_combinations_dic = self.combination_cognition(self.player_read)
        tem_read_value = self.read_value(self.player_read)
        self.player_combinations_dic = copy.deepcopy(tem_combinations_dic)
        self.player_read_value = copy.deepcopy(tem_read_value)

        tem_combinations_dic = self.combination_cognition(self.dealer_read)
        tem_read_value = self.read_value(self.dealer_read)
        self.dealer_combinations_dic = copy.deepcopy(tem_combinations_dic)
        self.dealer_read_value = copy.deepcopy(tem_read_value)


        play_combination_list = []
        deal_combination_list = []
        for counter in self.player_combinations_dic:
            play_combination_list.append(self.player_combinations_dic[counter])
        for counter in self.dealer_combinations_dic:
            deal_combination_list.append(self.dealer_combinations_dic[counter])

        self.combination_dic["player_read"] = self.player_read
        self.combination_dic["dealer_read"] = self.dealer_read
        self.combination_dic["player_read_value"] = self.player_read_value
        self.combination_dic["dealer_read_value"] = self.dealer_read_value
        self.combination_dic["play_combination_list"] = play_combination_list
        self.combination_dic["deal_combination_list"] = deal_combination_list
        self.combination_dic["combination_list"] = self.combinations
        return self.combination_dic


if __name__ == '__main__':
    game_dic = {"currency": 1000}
    game_dic["player_card"] = ['Club_4', 'Diamond_6', 'Club_5']
    game_dic["dealer_card"] = ['Heart_K', 'Heart_Q', 'Heart_Q']
    test = Get_Combinations(game_dic)
    game_dic = test.solve_combination()
    for counter in game_dic:
        print(counter, ":", game_dic[counter], end='\n')
