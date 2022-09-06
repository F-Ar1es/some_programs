from requests import get as reqget
from jsonsearch import JsonSearch


def get_data():
    source = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    view = reqget(source)

    status = view
    initial_data = view.text

    data = JsonSearch(initial_data, mode='s')

    return status, data

def format_infomation():
    source_data = get_data()[1]
    need_list = ['enddate', 'url', 'copyright', 'title']
    information_list = []

    for i in need_list:
        data = source_data.search_all_value(key=i)[0]
        information_list.append(data)

    return information_list