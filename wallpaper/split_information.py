from ast import parse
from calendar import month
import get_information
from datetime import date
from dateutil.parser import parse

information = get_information.format_infomation()

def judge_today():
    '''
    返回值为
    '''
    date_from_source = information[0]
    init_date_from_source = parse(date_from_source).date()
    today = date.today()
    if init_date_from_source == today:
        return init_date_from_source
    else:
        return

def combine_url():
    postfix = information[1]
    prdfix = "https://www.bing.com"
    wallpaper_url = prdfix + postfix

    return wallpaper_url