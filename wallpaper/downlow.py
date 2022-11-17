import requests, final_url, datetime, os

def get_UHD_url():
    # get this url will get a image with 1920x1080 resolution
    # replace the original resolution parms in url to UHD will get a full resolution image url
    prefix = 'https://cn.bing.com'
    UHD_url = str(final_url.get_needed_infomation()[0]).replace("1920x1080", "UHD")
    full_url = str(prefix) + UHD_url
    return full_url

def get_image():
    # access full url with get method
    # save image to memory with data flow
    target_url = get_UHD_url()
    my_headers = { 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15' }

    response = requests.get(url=target_url, headers=my_headers)
    image_flow = response.content
    return image_flow

def save_image_flow():
    # save data flow to file in disk
    with open('./{}.jpg'.format(datetime.date.today(),), 'wb') as f:
        image_flow = get_image()
        f.write(image_flow)
        f.close()
    
    print('Bing今日壁纸 {} 保存成功，'.format(final_url.get_needed_infomation()[2]))
    print('{}'.format(final_url.get_needed_infomation()[1]))
    print("\n请按任意键退出~~~")
    os.system('pause')


if __name__ == '__main__':
    save_image_flow()