import tkinter
import tkinter.messagebox
# import split_information
import get_information
# from requests import get as reqget

# tkinter.messagebox.showinfo('提示','test')

location = get_information.format_infomation()[2]
description = get_information.format_infomation()[3]

tkinter.messagebox.showinfo('提示',location)