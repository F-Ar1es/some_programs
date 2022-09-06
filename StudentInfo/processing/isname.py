"""
暂时没用，后面用来判断输入，用于判断词语是否为人名
"""

import jieba.posseg as pseg


def isname(user_input):
    pair_word_list = pseg.lcut(user_input)
    for fullname, POS in pair_word_list:
        if POS == "nr":
            return True
    return False


if __name__ == "__main__":
    userinput = input("输入您的姓名：")
    print(isname(userinput))
