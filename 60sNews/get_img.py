import requests
import json
import datetime
import os

APIUrl = "https://api.03c3.cn/zb/api.php"

initial_data = requests.get(APIUrl)
data = json.loads(initial_data.text)

class color:
    '''
    颜色输出
    '''
    fail = '\033[31m' # 红色
    ok = '\033[32m' # 绿色
    running = '\033[34m' # 蓝色

def get_status():
    http_status = data['code']
    msg_status = data['msg']

    
    if http_status == 200:
        if msg_status == 'Success':
            print(color.ok + '连接成功')
            return True
    else:
        print(color.fail + '连接失败')
        a = 0
        return False

def get_imgurl():
    if get_status() == True:
        img_Url = data['imageUrl']
    return img_Url

def get_img():
    Url = get_imgurl()
    img = requests.get(url=Url, stream=True)
    img_flow = img.content
    return img_flow

def save_at_local():
    with open('./img.jpg', 'wb') as f:
        f.write(get_img())
    os.rename('img.jpg', '{}.jpg'.format(datetime.date.today()))
    print("保存成功，请在当前文件路径下查看")
              
    
if __name__ == '__main__':
    save_at_local()