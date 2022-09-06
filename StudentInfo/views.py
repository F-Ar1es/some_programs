import tkinter as tk
import json
from tkinter import ttk
from processing.db import db


class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.stu_num = tk.StringVar()
        self.name = tk.StringVar()
        self.name_pinyin = tk.StringVar()
        self.sex = tk.StringVar()
        self.birth = tk.StringVar()
        self.phone = tk.StringVar()
        self.id_card = tk.StringVar()
        self.original_class = tk.StringVar()
        self.original_director_and_phone = tk.StringVar()
        self.dormitory = tk.StringVar()
        self.emergency_contact_and_phone = tk.StringVar()
        self.time_in_elite = tk.StringVar()
        self.status = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text="学号: ").grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.stu_num).grid(row=1, column=2, pady=10)

        tk.Label(self, text="姓名: ").grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)

        tk.Label(self, text="姓名全拼: ").grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.name_pinyin).grid(row=3, column=2, pady=10)

        tk.Label(self, text="性别: ").grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)

        tk.Label(self, text="出生日期: ").grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.birth).grid(row=5, column=2, pady=10)

        tk.Label(self, text="电话: ").grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.phone).grid(row=6, column=2, pady=10)

        tk.Label(self, text="身份证号: ").grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.id_card).grid(row=7, column=2, pady=10)

        tk.Label(self, text="原班级: ").grid(row=8, column=1, pady=10)
        tk.Entry(self, textvariable=self.original_class).grid(row=8, column=2, pady=10)

        tk.Label(self, text="原班主任和电话: ").grid(row=9, column=1, pady=10)
        tk.Entry(self, textvariable=self.original_director_and_phone).grid(row=9, column=2, pady=10)

        tk.Label(self, text="宿舍: ").grid(row=10, column=1, pady=10)
        tk.Entry(self, textvariable=self.dormitory).grid(row=10, column=2, pady=10)

        tk.Label(self, text="紧急联系人和电话: ").grid(row=11, column=1, pady=10)
        tk.Entry(self, textvariable=self.emergency_contact_and_phone).grid(row=11, column=2, pady=10)

        tk.Label(self, text="精英班时间: ").grid(row=12, column=1, pady=10)
        tk.Entry(self, textvariable=self.time_in_elite).grid(row=12, column=2, pady=10)

        tk.Button(self, text="添 加 信 息", command=self.recode_info).grid(row=13, column=2, pady=10)

        tk.Label(self, textvariable=self.status).grid(row=13, column=1, pady=10, stick=tk.E)

    def recode_info(self):
        stu = {
            "stu_num": self.stu_num.get(), "name": self.name.get(), "name_pinyin": self.name_pinyin.get(),
            "sex": self.sex.get(), "birth": self.birth.get(), "phone": self.phone.get(), "id_card": self.id_card.get(),
            "original_class": self.original_class.get(),
            "original_director_and_phone": self.original_director_and_phone.get(),
            "dormitory": self.dormitory.get(), "emergency_contact_and_phone": self.emergency_contact_and_phone.get(),
            "time_in_elite": self.time_in_elite.get()
        }

        self.stu_num.set('')
        self.name.set('')
        self.name_pinyin.set('')
        self.sex.set('')
        self.birth.set('')
        self.phone.set('')
        self.id_card.set('')
        self.original_class.set('')
        self.original_director_and_phone.set('')
        self.dormitory.set('')
        self.emergency_contact_and_phone.set('')
        self.time_in_elite.set('')

        db.insert(stu)

        item_list = []
        load_dict = json.loads(
            open('./Students_Info_DB.json', mode='r', encoding='utf-8').read())
        for i in range(len(load_dict)):
            stu_num = load_dict[i]['stu_num']
            name = load_dict[i]['name']
            name_pinyin = load_dict[i]['name_pinyin']
            sex = load_dict[i]['sex']
            birth = load_dict[i]['birth']
            phone = load_dict[i]['phone']
            id_card = load_dict[i]['id_card']
            original_class = load_dict[i]['original_class']
            original_director_and_phone = load_dict[i]['original_director_and_phone']
            dormitory = load_dict[i]['dormitory']
            emergency_contact_and_phone = load_dict[i]['emergency_contact_and_phone']
            time_in_elite = load_dict[i]['time_in_elite']

            item_dict = {'stu_num': stu_num, 'name': name, 'name_pinyin': name_pinyin, 'sex': sex, 'birth': birth,
                         'phone': phone, 'id_card': id_card, 'original_class': original_class,
                         'original_director_and_phone': original_director_and_phone, 'dormitory': dormitory,
                         'emergency_contact_and_phone': emergency_contact_and_phone, 'time_in_elite': time_in_elite}

            item_list.append(item_dict)

        item_list.append(stu)

        json.dump(item_list, open('./Students_Info_DB.json', 'w', encoding='utf-8'),
                  ensure_ascii=False)

        self.status.set('写入学生信息成功')


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

    def create_page(self):
        columns = ("stu_num", "name", "name_pinyin", "sex", "birth", "phone", "id_card", "original_class",
                   "original_director_and_phone", "dormitory", "emergency_contact_and_phone", "time_in_elite")

        columns_values = (
            "学号", "姓名", "姓名全拼", "性别", "出生日期", "电话", "身份证号", "原班级", "原班主任和电话", "宿舍",
            "紧急联系人和电话", "精英班时间")

        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)

        self.tree_view.column('stu_num', width=110, anchor='center')
        self.tree_view.column('name', width=60, anchor='center')
        self.tree_view.column('name_pinyin', width=110, anchor='center')
        self.tree_view.column('sex', width=50, anchor='center')
        self.tree_view.column('birth', width=120, anchor='center')
        self.tree_view.column('phone', width=130, anchor='center')
        self.tree_view.column('id_card', width=180, anchor='center')
        self.tree_view.column('original_class', width=240, anchor='center')
        self.tree_view.column('original_director_and_phone', width=180, anchor='center')
        self.tree_view.column('dormitory', width=70, anchor='center')
        self.tree_view.column('emergency_contact_and_phone', width=180, anchor='center')
        self.tree_view.column('time_in_elite', width=250, anchor='center')

        self.tree_view.heading('stu_num', text='学号')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('name_pinyin', text='姓名全拼')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('birth', text='出生日期')
        self.tree_view.heading('phone', text='电话')
        self.tree_view.heading('id_card', text='身份证号')
        self.tree_view.heading('original_class', text='班级')
        self.tree_view.heading('original_director_and_phone', text='原班主任和电话')
        self.tree_view.heading('dormitory', text='宿舍')
        self.tree_view.heading('emergency_contact_and_phone', text='紧急联系人和电话')
        self.tree_view.heading('time_in_elite', text='精英班时间')

        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data_frame()

        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def show_data_frame(self):
        # 删除旧的节点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        students = db.all()
        index = 0
        for stu in students:
            self.tree_view.insert('', index + 1, values=(
                stu['stu_num'], stu['name'], stu['name_pinyin'], stu['sex'], stu['birth'], stu['phone'], stu['id_card'],
                stu['original_class'], stu['original_director_and_phone'], stu['dormitory'],
                stu['emergency_contact_and_phone'], stu['time_in_elite']))


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.stu_num = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据学号删除数据').pack()
        tk.Entry(self, textvariable=self.stu_num).pack()
        tk.Button(self, text="删除", command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        stu_num = self.stu_num.get()
        flag, message = db.delete_by_number(stu_num)
        file = json.loads(open('./Students_Info_DB.json', mode='r', encoding='utf-8').read())
        info = []
        for i in file:
            if i['stu_num'] == stu_num:
                file.remove(i)
        json.dump(file, open('./Students_Info_DB.json', mode='w', encoding='utf-8'), ensure_ascii=False)
        self.status.set(message)


class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.stu_num = tk.StringVar()
        self.name = tk.StringVar()
        self.name_pinyin = tk.StringVar()
        self.sex = tk.StringVar()
        self.birth = tk.StringVar()
        self.phone = tk.StringVar()
        self.id_card = tk.StringVar()
        self.original_class = tk.StringVar()
        self.original_director_and_phone = tk.StringVar()
        self.dormitory = tk.StringVar()
        self.emergency_contact_and_phone = tk.StringVar()
        self.time_in_elite = tk.StringVar()
        self.status = tk.StringVar()

        self.create_page()

    def create_page(self):
        # tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text="学号: ").grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.stu_num).grid(row=1, column=2, pady=10)

        tk.Label(self, text="姓名: ").grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)

        tk.Label(self, text="姓名全拼: ").grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.name_pinyin).grid(row=3, column=2, pady=10)

        tk.Label(self, text="性别: ").grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)

        tk.Label(self, text="出生日期: ").grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.birth).grid(row=5, column=2, pady=10)

        tk.Label(self, text="电话: ").grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.phone).grid(row=6, column=2, pady=10)

        tk.Label(self, text="身份证号: ").grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.id_card).grid(row=7, column=2, pady=10)

        tk.Label(self, text="原班级: ").grid(row=8, column=1, pady=10)
        tk.Entry(self, textvariable=self.original_class).grid(row=8, column=2, pady=10)

        tk.Label(self, text="原班主任和电话: ").grid(row=9, column=1, pady=10)
        tk.Entry(self, textvariable=self.original_director_and_phone).grid(row=9, column=2, pady=10)

        tk.Label(self, text="宿舍: ").grid(row=10, column=1, pady=10)
        tk.Entry(self, textvariable=self.dormitory).grid(row=10, column=2, pady=10)

        tk.Label(self, text="紧急联系人和电话: ").grid(row=11, column=1, pady=10)
        tk.Entry(self, textvariable=self.emergency_contact_and_phone).grid(row=11, column=2, pady=10)

        tk.Label(self, text="精英班时间: ").grid(row=12, column=1, pady=10)
        tk.Entry(self, textvariable=self.time_in_elite).grid(row=12, column=2, pady=10)

        tk.Button(self, text="查 询", command=self.search_user).grid(row=13, column=2, pady=10)
        # tk.Button(self, text="修 改", command=self.change_user).grid(row=13, column=2, pady=10)

        tk.Label(self, textvariable=self.status).grid(row=14, column=1, pady=10, stick=tk.E)

    def search_user(self):
        flag, info = db.search_by_number(self.stu_num.get())
        if flag:
            self.stu_num.set(info['stu_num'])
            self.name.set(info['name'])
            self.name_pinyin.set(info['name_pinyin'])
            self.sex.set(info['sex'])
            self.birth.set(info['birth'])
            self.phone.set(info['phone'])
            self.id_card.set(info['id_card'])
            self.original_class.set(info['original_class'])
            self.original_director_and_phone.set(info['original_director_and_phone'])
            self.dormitory.set(info['dormitory'])
            self.emergency_contact_and_phone.set(info['emergency_contact_and_phone'])
            self.time_in_elite.set(info['time_in_elite'])
            self.status.set('数据查询成功')
        else:
            self.status.set(info)

    """
    以下注释函数用来修改数据，但是其中逻辑尚未理清
    """

    # def change_user(self):
    #     stu = {
    #         "stu_num": self.stu_num.get(), "name": self.name.get(), "name_pinyin": self.name_pinyin.get(),
    #         "sex": self.sex.get(), "birth": self.birth.get(), "phone": self.phone.get(), "id_card": self.id_card.get(),
    #         "original_class": self.original_class.get(),
    #         "original_director_and_phone": self.original_director_and_phone.get(),
    #         "dormitory": self.dormitory.get(), "emergency_contact_and_phone": self.emergency_contact_and_phone.get(),
    #         "time_in_elite": self.time_in_elite.get()
    #     }
    #
    #     self.stu_num.set('')
    #     self.name.set('')
    #     self.name_pinyin.set('')
    #     self.sex.set('')
    #     self.birth.set('')
    #     self.phone.set('')
    #     self.id_card.set('')
    #     self.original_class.set('')
    #     self.original_director_and_phone.set('')
    #     self.dormitory.set('')
    #     self.emergency_contact_and_phone.set('')
    #     self.time_in_elite.set('')
    #
    #     db.update(stu)
    #
    #     item_list = []
    #     load_dict = json.loads(open('D:\\Python_Project\\StudentInfo\\Students_Info_DB.json', mode='r', encoding='utf-8').read())
    #     for i in range(len(load_dict)):
    #         stu_num = load_dict[i]['stu_num']
    #         name = load_dict[i]['name']
    #         name_pinyin = load_dict[i]['name_pinyin']
    #         sex = load_dict[i]['sex']
    #         birth = load_dict[i]['birth']
    #         phone = load_dict[i]['phone']
    #         id_card = load_dict[i]['id_card']
    #         original_class = load_dict[i]['original_class']
    #         original_director_and_phone = load_dict[i]['original_director_and_phone']
    #         dormitory = load_dict[i]['dormitory']
    #         emergency_contact_and_phone = load_dict[i]['emergency_contact_and_phone']
    #         time_in_elite = load_dict[i]['time_in_elite']
    #
    #         item_dict = {'stu_num': stu_num, 'name': name, 'name_pinyin': name_pinyin, 'sex': sex, 'birth': birth,
    #                      'phone': phone, 'id_card': id_card, 'original_class': original_class,
    #                      'original_director_and_phone': original_director_and_phone, 'dormitory': dormitory,
    #                      'emergency_contact_and_phone': emergency_contact_and_phone, 'time_in_elite': time_in_elite}
    #
    #         item_list.append(item_dict)
    #
    #     item_list.append(stu)
    #
    #     json.dump(item_list, open('D:\\Python_Project\\StudentInfo\\Students_Info_DB.json', 'w', encoding='utf-8'),
    #               ensure_ascii=False)
    #
    #     self.status.set('修改学生信息成功')

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='关于作品: 本作品由tkinter制作').pack()
        tk.Label(self, text='关于作者: Carl').pack()
        tk.Label(self, text='参考作者: Bilibili-群里最弱的萌新').pack()