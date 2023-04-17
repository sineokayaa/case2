"""
Title
Group:
Sineokaya Anastasia
Varfolomeeva Viktoria
"""
import RU_LOCAL as RU

t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, tax = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


def non_resident():
    global t_7
    global t_8
    global t_9
    global tax
    ans_16 = input(RU.QUESTION_16).lower()
    if ans_16 == 'да':
        ans_17 = input(RU.QUESTION_17).lower()
        if ans_17 == 'да':
            ans_18 = float(input(RU.QUESTION_18))
        else:
            ans_18 = 0
        ans_19 = input(RU.QUESTION_19).lower()
        if ans_19 == 'да':
            ans_20 = float(input(RU.QUESTION_20))
        else:
            ans_20 = 0
        ans_21 = input(RU.QUESTION_21).lower()
        if ans_21 == 'да':
            ans_22 = float(input(RU.QUESTION_22))
        else:
            ans_22 = 0
        ans_23 = input(RU.QUESTION_23).lower()
        if ans_23 == 'да':
            ans_24 = float(input(RU.QUESTION_24))
        else:
            ans_24 = 0
        ans_25 = input(RU.QUESTION_25).lower()
        if ans_25 == 'да':
            ans_26 = float(input(RU.QUESTION_26))
        else:
            ans_26 = 0
        ans_27 = input(RU.QUESTION_27).lower()
        if ans_27 == 'да':
            ans_28 = float(input(RU.QUESTION_28))
        else:
            ans_28 = 0
        t_7 = (ans_18 + ans_20 + ans_22 + ans_24 + ans_26 + ans_28) * 0.13
        ans_29 = input(RU.QUESTION_29).lower()
        if ans_29 == 'да':
            ans_30 = float(input(RU.QUESTION_30))
            t_8 = ans_30 * 0.3
        else:
            t_8 = 0
        ans_31 = input(RU.QUESTION_31)
        if ans_31 == 'да':
            ans_32 = float(input(RU.QUESTION_32))
            t_8 = ans_32 * 0.3
        else:
            t_8 = 0
        tax = t_7 + t_8 + t_9
        return tax


ans_1 = input(RU.QUESTION_1).lower()
if ans_1 == 'да':
    ans_2 = input(RU.QUESTION_2).lower()
    if ans_2 == 'да':
        print(RU.CONCLUSION_1)
        t = non_resident()
    else:
        print(RU.CONCLUSION_2)
        ans_3 = float(input(RU.QUESTION_3))
        if 4000 <= ans_3 < 5_000_000:
            t_1 = ans_3 * 0.13
        elif ans_3 >= 5_000_000:
            t_1 = ans_3 * 0.15
        else:
            t_1 = 0
        ans_4 = float(input(RU.QUESTION_4))
        if 4000 <= ans_4 < 5_000_000:
            t_2 = ans_4 * 0.13
        elif ans_4 >= 5_000_000:
            t_2 = ans_4 * 0.15
        else:
            t_2 = 0
        ans_5 = input(RU.QUESTION_5).lower()
        if ans_5 == 'да':
            ans_5_2 = float(input(RU.QUESTION_5_2))
            t_3 = 0.13 * ans_5_2
        else:
            t_3 = 0
        ans_6 = input(RU.QUESTION_6).lower()
        if ans_6 == 'да':
            ans_6_2 = input(RU.QUESTION_6_2).lower()
            if ans_6_2 == 'да':
                t_4 = 0
            else:
                ans_6_3 = float(input(RU.QUESTION_6_3))
                t_4 = 0.13 * ans_6_3
        else:
            t_4 = 0
        ans_7 = input(RU.QUESTION_7).lower()
        if ans_7 == 'да':
            ans_8 = input(RU.QUESTION_8).lower()
            if ans_8 == 'да':
                ans_9 = int(input(RU.QUESTION_9))
                if ans_9 >= 2:
                    t_5 = 0
                else:
                    ans_10 = float(input(RU.QUESTION_10))
                    t_5 = ans_10 * 0.13
            else:
                ans_11 = float(input(RU.QUESTION_11))
                t_5 = ans_11 * 0.13
        else:
            t_5 = 0
        ans_12 = input(RU.QUESTION_12).lower()
        if ans_12 == 'да':
            ans_13 = float(input(RU.QUESTION_13))
            ans_14 = float(input(RU.QUESTION_14))
            ans_15 = float(input(RU.QUESTION_15))
            t_6 = (ans_13 + ans_14 + ans_15) * 0.13
        else:
            t_6 = 0
else:
    tax = non_resident()
taxes = t_1 + t_2 + t_3 + t_4 + t_5 + t_6 + tax
print(RU.QUESTION_33, taxes)
