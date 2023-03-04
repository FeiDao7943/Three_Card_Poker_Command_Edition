# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import numpy as np
import random
import copy


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class Generator:
    def __init__(self, input_dic):
        self.gen_dic = copy.deepcopy(input_dic)
        self.dealer_card_code = None
        self.player_card_code = None
        self.dealer_card = ["", "", ""]
        self.player_card = ["", "", ""]
        self.repertory = []
        self.group = ["Diamond", "Heart", "Spade", "Club"]
        self.value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def generate_repertory(self):
        for counter_group in range(len(self.group)):
            for counter_value in range(len(self.value)):
                self.repertory.append(str(self.group[counter_group]) \
                                      + "_" + str(self.value[counter_value]))

    def deal_card(self, txt=None):
        self.generate_repertory()
        card_num = [num for num in range(52)]
        np.random.shuffle(card_num)
        card_code_list = card_num[:6]
        self.player_card_code = card_code_list[:3]
        self.dealer_card_code = card_code_list[3:]

        for counter in range(len(self.player_card_code)):
            self.player_card[counter] = self.repertory[self.player_card_code[counter]]
            self.dealer_card[counter] = self.repertory[self.dealer_card_code[counter]]

        self.gen_dic['player_card'] = self.player_card
        self.gen_dic['dealer_card'] = self.dealer_card
        return self.gen_dic

        if txt:
            file = open("test_file/referee_test.txt", "a+")
            file.write(str(self.player_card))
            file.write(",")
            file.write(str(self.dealer_card))
            file.write(",\n")
            file.close()


if __name__ == '__main__':
    game_dic = {"currency": 1000}
    test = Generator(game_dic)
    game_dic = test.deal_card(txt=False)
    for counter in game_dic:
        print(counter, ":", game_dic[counter], end='\n')


