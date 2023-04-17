"""
Title
Group:
Sineokaya Anastasia
Varfolomeeva Viktoria
"""
import RU_LOCAL as RU

ans_1 = input(RU.QUESTION_1).lower()
if ans_1 == 'да':
    ans_2 = input(RU.QUESTION_2).lower()
    if ans_2 == 'да':
        print(RU.CONCLUSION_1)
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
    ans_5 = float(input(RU.QUESTION_5))
    t_3 = 0.13 * ans_5
    ans_6 = float(input(RU.QUESTION_6))
    t_4 = 0.13 * ans_6
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
print(t_1 + t_2 + t_3 + t_4 + t_5 + t_6)





