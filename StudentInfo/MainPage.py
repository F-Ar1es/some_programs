import tkinter as tk
from views import InsertFrame, SearchFrame, DeleteFrame, ChangeFrame, AboutFrame


class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('学生信息管理系统 v0.0.1')
        self.root.geometry('1000x800')
        self.create_page()

    def create_page(self):
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.change_frame = ChangeFrame(self.root)
        self.about_frame = AboutFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入', command=self.show_insert)
        menubar.add_command(label='查询', command=self.show_search)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='修改（内容未完成，只有 获取 功能）', command=self.show_change)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def show_insert(self):
        self.insert_frame.pack()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()

    def show_search(self):
        self.search_frame.pack()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()

    def show_delete(self):
        self.delete_frame.pack()
        self.search_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()

    def show_about(self):
        self.about_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()

    def show_change(self):
        self.change_frame.pack()
        self.about_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
