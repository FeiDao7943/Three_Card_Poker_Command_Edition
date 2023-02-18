# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

class Referee_method:
    def __init__(self, player_card, dealer_card):
        self.read_value = None
        self.combinations = ["Pair", "Flush", "Straight", "Three of a Kind", "Straight Flush"]
        self.score_dic = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                          "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
                          "Pair": 100, "Flush": 200, "Straight": 300,
                          "Three of a Kind": 400, "Straight Flush": 500}
        self.pair_flag = 0
        self.flush_flag = 0
        self.straight_flag = 0
        self.three_of_a_kind_flag = 0
        self.straight_flush_flag = 0
        self.player_card = player_card
        self.dealer_card = dealer_card
        self.player_read = []
        self.dealer_read = []
        self.player_score = 0
        self.dealer_score = 0
        self.dealer_max = 0

    def read_card(self):
        for counter in range(len(self.player_card)):
            self.player_read.append(self.player_card[counter].split("_", 2))
            self.dealer_read.append(self.dealer_card[counter].split("_", 2))
        # print(self.player_read)
        # print(self.dealer_read)

    def judgement(self, role_card_read):
        """judgement"""
        self.pair_flag = 0
        self.flush_flag = 0
        self.straight_flag = 0
        self.three_of_a_kind_flag = 0
        self.straight_flush_flag = 0
        '''Pair Judge'''
        if (role_card_read[1][1] == role_card_read[0][1]) or \
                (role_card_read[1][1] == role_card_read[2][1]) or \
                (role_card_read[0][1] == role_card_read[2][1]):
            self.pair_flag = 1

        '''Flush Judge'''
        if (role_card_read[1][0] == role_card_read[0][0]) and \
                (role_card_read[1][0] == role_card_read[2][0]):
            self.flush_flag = 1

        '''Straight Judge'''
        read_value = [0, 0, 0]
        for counter in range(len(read_value)):
            read_value[counter] = int(self.score_dic[role_card_read[counter][1]])
        # print(read_value)
        tem_max = 0
        tem_mid = 0
        tem_min = 100
        for counter in range(len(read_value)):
            if read_value[counter] > tem_max:
                tem_max = read_value[counter]
            if read_value[counter] < tem_min:
                tem_min = read_value[counter]

        for counter in range(len(read_value)):
            if (read_value[counter] < tem_max) and (read_value[counter] > tem_min):
                tem_mid = read_value[counter]

        read_value[0] = tem_min
        read_value[1] = tem_mid
        read_value[2] = tem_max

        self.dealer_max = tem_max
        self.read_value = read_value

        # print(read_value)
        if (read_value[0] + 1 == read_value[1]) and \
                (read_value[1] + 1 == read_value[2]):
            self.straight_flag = 1

        '''Three of a Kind Judge'''
        if (role_card_read[1][1] == role_card_read[0][1]) and \
                (role_card_read[1][1] == role_card_read[2][1]):
            self.pair_flag = 0
            self.three_of_a_kind_flag = 1

        '''Straight Flush Judge'''
        if self.straight_flag * self.flush_flag == 1:
            self.straight_flush_flag = 1
            self.straight_flag = 0
            self.flush_flag = 0

        # print(role_card_read)
        # print("Straight Flush  : ", bool(self.straight_flush_flag))
        # print("Three of a Kind : ", bool(self.three_of_a_kind_flag))
        # print("Straight        : ", bool(self.straight_flag))
        # print("Flush           : ", bool(self.flush_flag))
        # print("Pair            : ", bool(self.pair_flag))

    def judgement_2(self, role_card_read):
        """judgement"""
        self.pair_flag = 0
        self.flush_flag = 0
        self.straight_flag = 0
        self.three_of_a_kind_flag = 0
        self.straight_flush_flag = 0
        '''Pair Judge'''
        if (role_card_read[1][1] == role_card_read[0][1]) or \
                (role_card_read[1][1] == role_card_read[2][1]) or \
                (role_card_read[0][1] == role_card_read[2][1]):
            self.pair_flag = 1

        '''Flush Judge'''
        if (role_card_read[1][0] == role_card_read[0][0]) and \
                (role_card_read[1][0] == role_card_read[2][0]):
            self.flush_flag = 1

        '''Straight Judge'''
        read_value = [0, 0, 0]
        for counter in range(len(read_value)):
            read_value[counter] = int(self.score_dic[role_card_read[counter][1]])
        # print(read_value)
        tem_max = 0
        tem_mid = 0
        tem_min = 100
        for counter in range(len(read_value)):
            if read_value[counter] > tem_max:
                tem_max = read_value[counter]
            if read_value[counter] < tem_min:
                tem_min = read_value[counter]

        for counter in range(len(read_value)):
            if (read_value[counter] < tem_max) and (read_value[counter] > tem_min):
                tem_mid = read_value[counter]

        read_value[0] = tem_min
        read_value[1] = tem_mid
        read_value[2] = tem_max

        self.read_value = read_value

        # print(read_value)
        if (read_value[0] + 1 == read_value[1]) and \
                (read_value[1] + 1 == read_value[2]):
            self.straight_flag = 1

        '''Three of a Kind Judge'''
        if (role_card_read[1][1] == role_card_read[0][1]) and \
                (role_card_read[1][1] == role_card_read[2][1]):
            self.pair_flag = 0
            self.three_of_a_kind_flag = 1

        '''Straight Flush Judge'''
        if self.straight_flag * self.flush_flag == 1:
            self.straight_flush_flag = 1
            self.straight_flag = 0
            self.flush_flag = 0

        # print(role_card_read)
        # print("Straight Flush  : ", bool(self.straight_flush_flag))
        # print("Three of a Kind : ", bool(self.three_of_a_kind_flag))
        # print("Straight        : ", bool(self.straight_flag))
        # print("Flush           : ", bool(self.flush_flag))
        # print("Pair            : ", bool(self.pair_flag))

    def score_calculate(self, role_card_read):
        role_score = 0
        '''Normal'''
        if (self.straight_flush_flag + self.three_of_a_kind_flag + self.straight_flag +
            self.flush_flag + self.pair_flag) == 0:
            for counter in range(len(role_card_read)):
                role_score = float(self.read_value[2])
        '''Pair'''
        if self.pair_flag:
            role_score += self.score_dic["Pair"]
            if self.read_value[0] == self.read_value[1]:
                role_score += int(self.read_value[0])
            if self.read_value[0] == self.read_value[2]:
                role_score += int(self.read_value[2])
            if self.read_value[1] == self.read_value[2]:
                role_score += int(self.read_value[1])

        '''Flush'''
        if self.flush_flag:
            role_score += self.score_dic["Flush"]
            role_score += float(self.read_value[2])

        '''Straight'''
        if self.straight_flag:
            role_score += self.score_dic["Straight"]
            role_score += float(self.read_value[2])

        '''Three of a Kind'''
        if self.three_of_a_kind_flag:
            role_score += self.score_dic["Three of a Kind"]
            role_score += float(self.read_value[2])

        '''Straight Flush'''
        if self.straight_flush_flag:
            role_score += self.score_dic["Straight Flush"]
            role_score += float(self.read_value[2])

        # print(role_score)
        return role_score

    def score_calculate_2(self, role_card_read):
        role_score = 0
        '''Normal'''
        if (self.straight_flush_flag + self.three_of_a_kind_flag + self.straight_flag +
            self.flush_flag + self.pair_flag) == 0:
            for counter in range(len(role_card_read)):
                role_score = int(self.read_value[2]) + \
                             int(self.read_value[1])
        '''Pair'''
        if self.pair_flag:
            role_score += self.score_dic["Pair"]
            if self.read_value[0] == self.read_value[1]:
                role_score += int(self.read_value[0])
            if self.read_value[0] == self.read_value[2]:
                role_score += int(self.read_value[2])
            if self.read_value[1] == self.read_value[2]:
                role_score += int(self.read_value[1])

        '''Flush'''
        if self.flush_flag:
            role_score += self.score_dic["Flush"]
            role_score += float(self.read_value[1])

        '''Straight'''
        if self.straight_flag:
            role_score += self.score_dic["Straight"]
            role_score += float(self.read_value[1])

        '''Three of a Kind'''
        if self.three_of_a_kind_flag:
            role_score += self.score_dic["Three of a Kind"]
            role_score += float(self.read_value[1])

        '''Straight Flush'''
        if self.straight_flush_flag:
            role_score += self.score_dic["Straight Flush"]
            role_score += float(self.read_value[1])

        # print(role_score)
        return role_score

    def score_calculate_3(self, role_card_read):
        role_score = 0
        '''Normal'''
        if (self.straight_flush_flag + self.three_of_a_kind_flag + self.straight_flag +
            self.flush_flag + self.pair_flag) == 0:
            for counter in range(len(role_card_read)):
                role_score = int(self.read_value[2]) + \
                             int(self.read_value[1]) + \
                             int(self.read_value[0])
        '''Pair'''
        if self.pair_flag:
            role_score += self.score_dic["Pair"]
            if self.read_value[0] == self.read_value[1]:
                role_score += int(self.read_value[2])
            if self.read_value[0] == self.read_value[2]:
                role_score += int(self.read_value[1])
            if self.read_value[1] == self.read_value[2]:
                role_score += int(self.read_value[0])

        '''Flush'''
        if self.flush_flag:
            role_score += self.score_dic["Flush"]
            role_score += float(self.read_value[0])

        '''Straight'''
        if self.straight_flag:
            role_score += self.score_dic["Straight"]
            role_score += float(self.read_value[0])

        '''Three of a Kind'''
        if self.three_of_a_kind_flag:
            role_score += self.score_dic["Three of a Kind"]
            role_score += float(self.read_value[0])

        '''Straight Flush'''
        if self.straight_flush_flag:
            role_score += self.score_dic["Straight Flush"]
            role_score += float(self.read_value[0])

        # print(role_score)
        return role_score

    def final(self, curr):
        currency = curr
        currency_2 = currency
        ante = int(input("Ante: "))
        currency -= ante
        pair_plus = int(input("Pair Plus: "))
        currency -= pair_plus
        self.read_card()
        self.judgement(self.player_read)
        self.player_score = self.score_calculate(self.player_read)
        # print(self.player_score)

        self.judgement(self.dealer_read)
        self.dealer_score = self.score_calculate(self.dealer_read)
        # print(self.dealer_score)

        print("\033[1mPlayer Card: \033[0m", self.player_card)
        # print("Player Card", self.player_score)
        # print("Dealer Card", self.dealer_score)
        self.judgement_2(self.player_read)

        if self.player_score > self.dealer_score:
            # print("Player Win!")
            result = "P"
        if self.player_score < self.dealer_score:
            # print("Dealer Win!")
            result = "D"
        if self.player_score == self.dealer_score:
            self.judgement(self.player_read)
            self.player_score = self.score_calculate_2(self.player_read)

            self.judgement(self.dealer_read)
            self.dealer_score = self.score_calculate_2(self.dealer_read)
            # print("Player Card", self.player_card)
            # print("Dealer Card", self.dealer_card)
            # print("Player Card", self.player_score)
            # print("Dealer Card", self.dealer_score)
            if self.player_score > self.dealer_score:
                # print("Player Win!")
                result = "P"
            if self.player_score < self.dealer_score:
                # print("Dealer Win!")
                result = "D"
            if self.player_score == self.dealer_score:
                self.judgement(self.player_read)
                self.player_score = self.score_calculate_3(self.player_read)

                self.judgement(self.dealer_read)
                self.dealer_score = self.score_calculate_3(self.dealer_read)
                # print("Player Card", self.player_card)
                # print("Dealer Card", self.dealer_card)
                # print("Player Card", self.player_score)
                # print("Dealer Card", self.dealer_score)
                if self.player_score > self.dealer_score:
                    # print("Player Win!")
                    result = "P"
                if self.player_score < self.dealer_score:
                    # print("Dealer Win!")
                    result = "D"
                if self.player_score == self.dealer_score:
                    # print("Draw!")
                    result = "S"
        play = int(input("Play Wager: "))
        currency -= play

        print("\033[1mDealer Card: \033[0m", self.dealer_card)
        if result == "P":
            print("\033[1;32mPlayer Win!\033[0m")
            print("List: ", end="")
            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) == 0:

                if self.dealer_max <= 11:
                    currency += 2 * play + 1 * ante
                    print("+ 1xPlay - 1xPair Plus=>", end="")

                if self.dealer_max >= 12:
                    currency += 2 * play + 2 * ante
                    print("+ 1xPlay + 1xAnte - 1xPair Plus=>", end="")

            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) >= 1:

                if self.straight_flush_flag:
                    currency += 41 * pair_plus + 6 * ante + 6 * play
                    print("+ 5xPlay + 5xAnte + 40xPair Plus =>", end="")

                if self.three_of_a_kind_flag:
                    currency += 31 * pair_plus + 5 * ante + 5 * play
                    print("+ 4xPlay + 4xAnte + 30xPair Plus =>", end="")

                if self.straight_flag:
                    currency += 7 * pair_plus + 2 * ante + 2 * play
                    print("+ 1xPlay + 1xAnte + 6xPair Plus =>", end="")

                if self.flush_flag:
                    currency += 4 * pair_plus + 2 * play + 2 * ante
                    print("+ 1xPlay + 1xAnte + 3xPair Plus =>", end="")

                if self.pair_flag:
                    currency += 2 * pair_plus + 2 * play + 2 * ante
                    print("+ 1xPlay + 1xAnte + 1xPair Plus =>", end="")

        if result == "D":
            print("\033[1;31mDealer Win!\033[0m")
            print("List: ", end="")
            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) == 0:
                if self.dealer_max <= 11:
                    currency += ante
                    print("+ 1xAnte - 1xPlay - 1xPair Plus =>", end="")
                if self.dealer_max >= 12:
                    currency += 0
                    print("- 1xAnte - 1xPlay -1xPair Plus =>", end="")
            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) >= 1:

                if self.straight_flush_flag:
                    currency += 41 * pair_plus
                    print("+ 40xPair Plus =>", end="")
                if self.three_of_a_kind_flag:
                    currency += 31 * pair_plus
                    print("+ 30xPair Plus =>", end="")
                if self.straight_flag:
                    currency += 7 * pair_plus
                    print("+ 6xPair Plus =>", end="")

                if self.flush_flag:
                    currency += 4 * pair_plus
                    print("+ 3xPair Plus =>", end="")

                if self.pair_flag:
                    currency += 2 * pair_plus
                    print("+ 1xPair Plus =>", end="")

        if result == "S":
            print("\033[1;36mDraw!\033[0m")
            print("List: ", end="")
            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) == 0:
                if self.dealer_max <= 11:
                    currency += ante
                    print("+ 1xAnte - 1xPlay - 1xPair Plus =>", end="")
                if self.dealer_max >= 12:
                    currency += 0
                    print("+ 1xAnte - 1xPlay - 1xPair Plus =>", end="")
            if (self.straight_flush_flag + self.three_of_a_kind_flag
                + self.straight_flag + self.flush_flag + self.pair_flag) >= 1:

                if self.straight_flush_flag:
                    currency += 41 * pair_plus
                    print("+ 40xPair Plus =>", end="")
                if self.three_of_a_kind_flag:
                    currency += 31 * pair_plus
                    print("+ 30xPair Plus =>", end="")
                if self.straight_flag:
                    currency += 7 * pair_plus
                    print("+ 6xPair Plus =>", end="")

                if self.flush_flag:
                    currency += 4 * pair_plus
                    print("+ 3xPair Plus =>", end="")

                if self.pair_flag:
                    currency += 2 * pair_plus
                    print("+ 1xPair Plus =>", end="")

        if currency - currency_2 < 0:
            print(" -", str(currency_2 - currency))
        if currency - currency_2 > 0:
            print(" +", str(currency - currency_2))
        ante = 0
        play = 0
        pair_plus = 0
        if currency < 0:
            currency = 0

        return currency



        # if result != label:
        #     print("------------------------")
        #     correct += 1
        # return correct


if __name__ == '__main__':
    file = open("referee_test.txt", "r")
    all_text = file.readlines()
    correct = 0
    # for text in all_text:
    #     text = text.replace("[", "")
    #     text = text.replace("]", "")
    #     text = text.replace(" ", "")
    #     text = text.replace("'", "")
    #     text = text.replace("\n", "")
    #     text = text.split(",", 7)
    #     # print(text)
    #     test_player_card = [text[0], text[1], text[2]]
    #     test_dealer_card = [text[3], text[4], text[5]]
    #     label = text[6]
    #     test = Referee_method(test_player_card, test_dealer_card)
    #     test.final(label, correct)
    # print(correct)
