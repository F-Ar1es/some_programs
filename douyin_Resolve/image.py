import requests
import re
import time

def split_url(sharetext):
    sharetext = sharetext.replace("\n", "")
    # extractor = URLExtract()
    # shareurl = extractor.find_urls(sharetext)[0]
    shareurl = re.findall('[a-zA-z]+://[^\s]*', sharetext)[0]
    
    return shareurl

def change_url():
    '''
    将短地址转换为长地址
    返回值为 long_url 字符串
    '''
    
    try:
        r = requests.get(url=shareurl, headers=headers, allow_redirects=False)
        long_url = r.headers['location']
        return long_url
    
    except Exception as e:
        print("解析失败")
        print(e)

def get_image_url():
    '''
    获取没有水印的图片链接, 将链接写入列表中
    返回值: image_without_watermark_url 列表
    '''
    image_without_watermark_url = []

    url = change_url()
    
    if not url:
        return

    try:
        vid = url.split("/?")[0].split("video/")[1]
        xhr_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid}'
        
        r = requests.get(xhr_url, headers=headers).json()
        
        # video_url = r['item_list'][0]['images']['play_addr']['url_list'][0]
        all_image_url = r['item_list'][0]['images']
        '''类型为列表'''
        
        for items in all_image_url:
            for need in items:
                if need == "url_list":
                    image_without_watermark_url.append(items[need][0])

        return image_without_watermark_url
    
    except Exception as e:
        print("解析失败")
        print(e)
        
def download_image():
    '''
    循环列表中的链接, 下载图片
    '''
    name = 0
    
    for i in get_image_url():

        r = requests.get(i, headers=headers)
        content = r.content
        with open(f"{name}.png", "wb") as f:
            f.write(content)
            name += 1
    
if __name__ == "__main__":
    sharetext = input("请输入分享链接：")
    shareurl = split_url(sharetext)
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36", }
    try :
        download_image()
    except Exception as e:
        print("下载失败")
        print(e)