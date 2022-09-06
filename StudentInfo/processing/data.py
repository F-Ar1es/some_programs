"""
暂时没用，后续用来处理输入的数据
"""

from processing.isname import isname


class Students(object):
    def __init__(
            self, stu_num, name, name_pinyin, sex, birth, phone, id_card,
            major, class_num, original_director, original_director_phone, dormitory,
            emergency_contact, emergency_contact_phone,
            join_time, out_time, competition_mark,
            honor, others
    ):
        self.__stu_num = stu_num
        self.__name = name
        self.__name_pinyin = name_pinyin
        self.__sex = sex
        self.__birth = birth
        self.__phone = phone
        self.__id_card = id_card
        self.__major = major
        self.__class_num = class_num
        self.__original_director = original_director
        self.__original_director_phone = original_director_phone
        self.__dormitory = dormitory
        self.__emergency_contact = emergency_contact
        self.__emergency_contact_phone = emergency_contact_phone
        self.__join_time = join_time
        self.__out_time = out_time
        self.__competition_mark = competition_mark
        self.__honor = honor
        self.__others = others

    def student_info(self, stu_num, name, name_pinyin, sex, birth, phone, id_card):
        if isname(stu_num):
            self.__stu_num = stu_num

    def class_info(self, major, class_num, original_director, original_director_phone, dormitory):
        pass

    def emergency_info(self, emergency_contact, emergency_contact_phone):
        pass

    def elite_class_info(self, join_time, out_time, competition_mark, ):
        pass

    def other_info(self, honor, others):
        pass


# 测试
if __name__ == '__main__':
    pass
