import requests

def get_official_infomation():
    # defind requests needed params
    target_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    my_headers = { 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15' }

    # access api,
    # `get_infomation` recieved values
    # `infomation` change the recieved values to Dict data type
    get_infomation = requests.get(url=target_url, headers=my_headers)
    infomation = get_infomation.json()
    
    return infomation


def get_needed_infomation():
    # returned value get back a dict with two dict in it
    # get suffix description and title form first dict
    infomation_dirt = get_official_infomation().get('images')[0]
    suffix = infomation_dirt.get('url')
    description = infomation_dirt.get('copyright')
    title = infomation_dirt.get('title')

    return suffix, description, title

if __name__ == '__main__':
    get_needed_infomation()