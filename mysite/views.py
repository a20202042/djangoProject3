from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post
import json
import requests


def index(request):
    posts = Post.objects.all()
    myname = "月降雨量統計"
    data = [i for i in range(1, 43)]
    random.shuffle(data)
    lotto_numbers = data[0:6]
    special_number = data[6]
    return render(request, 'index.html', locals())


def show(request, id):
    try:
        target = Post.objects.get(id=id)
    except:

        return redirect("/")
    return render(request, "showpost.html", locals())


def weather(request, id):
    token = 'CWB-CF13E86E-3C39-4364-B74C-A79F63F31AE0'
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/C-B0025-001?Authorization=' + token + '&format=JSON&sort=dataTime&statistics=true" -H  "accept: application/json'
    Data = requests.get(url)
    DATA = json.loads(Data.text)
    DATA_2 = DATA['records']['location']
    all_local_weather = []
    key = {0: '鞍部', 1: '新竹', 2: '金門', 3: '大武', 4: '成功', 5: '板橋', 6: '彰化', 7: '臺中', 8: '日月潭', 9: '雲林', 10: '屏東',
           11: '花蓮', 12: '新屋', 13: '宜蘭', 14: '阿里山', 15: '桃園', 16: '基隆', 17: '臺東', 18: '苗栗', 19: '高雄', 20: '恆春',
           21: '臺北', 22: '竹子湖', 23: '梧棲', 24: '嘉義', 25: '蘭嶼', 26: '東吉島', 27: '澎湖', 28: '臺南', 29: '淡水', 30: '蘇澳',
           31: '玉山', 32: '彭佳嶼', 33: '馬祖', 34: '田中'}
    for i in key:
        if id == i:
            local = key[i]
    for item in DATA_2:
        # print(item['stationObsTimes']['stationObsTime'][-1])
        # print(item['stationObsTimes']['stationObsTime'][-1]['dataDate'])
        # print(item['stationObsTimes']['stationObsTime'][-1]['weatherElements']['precipitation'])
        # print(item['station']['stationName'])
        local_weather = {
            "rainfall": item['stationObsTimes']['stationObsTime'][-1]['weatherElements']['precipitation'],
            'local': item['station']['stationName'],
            "time": item['stationObsTimes']['stationObsTime'][-1]['dataDate']}
        all_local_weather.append(local_weather)
    for item in all_local_weather:
        if local == item['local']:
            local_weather = item
    a_all ,a_image_all =  gel_rainalll(local)
    print(a_all,a_image_all)
    return render(request, 'weather.html', locals())


def gel_rainalll(city):
    all_rain = {'臺北': [[256.0, 78.9, 285.7, 184.4, 186.7, 429.8, 174.6, 141.4, 428.5, 137.6, 111.6, 16.5],
                       [21.8, 123.7, 182.7, 121.5, 135.5, 649.7, 206.6, 166.2, 175.6, 368.6, 120.9, 66.9],
                       [255.8, 163.6, 37.3, 59.6, 42.0, 119.8, 190.3, 186.8, 321.9, 125.1, 64.4, 54.4],
                       [45.0, 64.1, 184.2, 115.1, 335.8, 419.5, 439.3, 212.4, 377.1, 27.1, 13.8, 136.2],
                       [38.6, 29.6, 245.5, 87.9, 405.8, 117.9, 133.5, 322.5, 129.5, 25.5, 21.5, 145.0]],
                '基隆': [[441.2, 422.2, 317.1, 192.9, 176.2, 255.0, 125.3, 112.3, 531.7, 814.9, 313.0, 139.6],
                       [254.7, 264.5, 288.8, 141.9, 229.1, 824.9, 67.9, 20.2, 188.8, 409.8, 708.2, 458.8],
                       [541.7, 360.5, 69.4, 108.7, 52.0, 244.5, 135.8, 92.0, 558.4, 403.5, 261.2, 578.0],
                       [382.1, 292.4, 209.1, 140.0, 404.2, 431.1, 102.3, 173.3, 659.1, 152.3, 219.0, 352.6],
                       [189.0, 161.7, 202.7, 223.8, 475.7, 91.7, 134.0, 212.0, 485.4, 505.0, 277.5, 936.5]],
                '臺中': [[204.9, 24.2, 194.6, 183.4, 100.3, 230.9, 166.7, 184.6, 126.2, 23.9, 74.2, 8.4],
                       [4.0, 20.8, 38.0, 98.8, 111.5, 894.0, 313.7, 69.0, 21.4, 53.5, 19.5, 8.0],
                       [103.5, 25.5, 35.5, 30.5, 73.0, 234.0, 347.0, 408.5, 20.0, 7.5, 10.0, 2.0],
                       [13.0, 11.0, 179.5, 115.5, 524.0, 480.0, 177.5, 768.0, 133.5, 11.5, 0.0, 94.5],
                       [20.0, 4.5, 55.0, 59.5, 306.5, 183.5, 93.5, 278.5, 74.0, 'T', 3.5, 41.5]],
                '南投': [[326.5, 42.0, 275.0, 239.0, 160.0, 443.0, 205.5, 179.3, 258.0, 75.6, 68.0, 21.5],
                       [4.0, 14.0, 57.5, 255.5, 347.5, 1013.0, 424.5, 183.5, 118.0, 85.0, 48.0, 17.5],
                       [150.0, 72.0, 45.0, 108.0, 95.0, 427.0, 316.0, 556.5, 128.5, 18.0, 24.5, 1.0],
                       [9.0, 6.5, 171.5, 135.0, 674.0, 754.5, 216.5, 664.5, 92.0, 9.5, 0.0, 138.0],
                       [11.5, 70.5, 90.0, 72.0, 508.0, 330.0, 239.0, 249.0, 81.0, 'T', 5.0, 51.0]]
                }
    year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December']
    year_2 = ['a_5', 'a_6', 'a_7', 'a_8', 'a_9']
    a_all = []
    a_image_all = {}
    data = {}
    for item in all_rain:
        if item == city:
            a_image_all.update({'a_5':all_rain[item][0]})
            a_image_all.update({'a_6':all_rain[item][1]})
            a_image_all.update({'a_7':all_rain[item][2]})
            a_image_all.update({'a_8':all_rain[item][3]})
            a_image_all.update({'a_9':all_rain[item][4]})
            for i in all_rain[item]:
                a_all.append({
                    year[0]: i[0],
                    year[1]: i[1],
                    year[2]: i[2],
                    year[3]: i[3],
                    year[4]: i[4],
                    year[5]: i[5],
                    year[6]: i[6],
                    year[7]: i[7],
                    year[8]: i[8],
                    year[9]: i[9],
                    year[10]: i[10],
                    year[11]: i[11],
                })
    return a_all ,a_image_all
