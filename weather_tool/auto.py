import requests as req
import json
import check_connetion

file = open('/key.txt', 'r')
key = file.read()

class color:
    '''
    颜色输出
    '''
    fail = '\033[31m' # 红色
    ok = '\033[32m' # 绿色
    running = '\033[34m' # 蓝色
    
def get_host_ip():
    """
    通过IP获得城市的经纬度
    """
    url = 'http://ip-api.com/json/'
    params = {'fields': 'status,lat,lon',}
    res = req.get(url=url, params=params)
    res_json = json.loads(res.text)

    if res_json['status'] == 'success':
        lat = round(res_json['lat'],2)
        lon = round(res_json['lon'],2)
        coord = '{},{}'.format(lon, lat)
    
    return coord

def get_city_id():
    """
    获取城市ID
    """
    city_name = get_host_ip()
    url = 'https://geoapi.qweather.com/v2/city/lookup?'
    params = {
        "location": city_name,
        "key": key,
    }
    res = req.get(url=url, params=params)
    res_json = json.loads(res.text)
    
    if res_json['code'] == '200':
        city_id = res_json['location'][0]['id']
        
    return city_id

def get_weather():
    """
    获取天气信息
    """
    city_id = get_city_id()
    url = 'https://devapi.qweather.com/v7/weather/now?'
    params = {
        "location": city_id,
        "key": key,
    }

    res = req.get(url=url, params=params)
    res_json = json.loads(res.text)
    
    data = res_json['now']

    if res_json['code'] == '200':
        updatetim = res_json['updateTime']
        temp = data['temp']
        body_feel = data['feelsLike']
        weather = data['text']
    
    return updatetim, temp, body_feel, weather
      
def output():
    """
    输出信息
    """
    updatetim, temp, body_feel, weather = get_weather()
    print('\n' + color.ok + '更新时间：' + updatetim)
    print(color.ok + '温度：' + temp)
    print(color.ok + '体感温度：' + body_feel)
    print(color.ok + '天气：' + weather + '\n')
        
if __name__ == '__main__':
    '''运行主程序'''
    if check_connetion.check_network_status() == 200:
        print('\n' + color.running + '正在查询天气信息...' + color.running)
        output()
    else:
        print(color.fail + "网络连接失败，请检查网络连接" +'\n')
        exit()