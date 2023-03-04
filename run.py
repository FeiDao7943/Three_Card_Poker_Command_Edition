# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
from generate_card import Generator
from combinations import Get_Combinations
from compare import Get_Compare


def limit_input(limit, value_name):
    pass_flag = 0
    while not pass_flag:
        try:
            locals()[value_name] = int(input("Input the %s: " % value_name))
            if locals()[value_name] <= limit:
                pass_flag = 1
            if locals()[value_name] > limit:
                print("Value of %s is over the limit." % value_name)
        except:
            print("Enter integral number.")
    return locals()[value_name]


def main():
    game_dic = {"currency": 1000}

    if game_dic["currency"] > 0:

        # Step 1, Generate the Cards
        step_1 = Generator(game_dic)
        game_dic = step_1.deal_card(txt=False)

        # Step 2, Cognition of Combinations
        step_2 = Get_Combinations(game_dic)
        game_dic = step_2.solve_combination()

        # Step 3, Compare The Cards
        step_3 = Get_Compare(game_dic)
        game_dic = step_3.solve_compare()

        for counter in game_dic:
            print(counter, ":", game_dic[counter], end='\n')

        # ante = limit_input(game_dic["currency"] / 2, "ante")
        # pair_plus = limit_input(game_dic["currency"] - 2 * ante, "pair_plus")


if __name__ == '__main__':
    main()
