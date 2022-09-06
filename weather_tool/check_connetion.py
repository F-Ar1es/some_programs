import requests

def check_network_status():
    try:
        rul = "https://geoapi.qweather.com/v2/city/lookup?"
        getback = requests.get(rul)
        return getback.status_code
    except:
        return False