import json
import requests

# token = 'CWB-CF13E86E-3C39-4364-B74C-A79F63F31AE0'
# url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/C-B0027-001?Authorization=' + token + '&weatherElement=precipitation&dataMonth=" -H  "accept: application/json'
# Data = requests.get(url)
# DATA = json.loads(Data.text)
# print(DATA)
# all_local_rainall = []
# data = {}
# for item in DATA_2:
#     print(item['stationObsTimes']['stationObsTime'][-1])
#     print(item['stationObsTimes']['stationObsTime'][-1]['dataDate'])
#     print(item['stationObsTimes']['stationObsTime'][-1]['weatherElements']['precipitation'])
#     print(item['station']['stationName'])
#     local = {i: item['station']['stationName']}
#     i = i + 1
#     data.update(local)
# print(data)
# def find(city):
#     for item in a:
#         if city == a[item]:
#             print(item)
# find('臺中')
# b_5 = '256.0 	78.9 	285.7 	184.4 	186.7 	429.8 	174.6 	141.4 	428.5 	137.6 	111.6 	16.5'.split()
# c_5 = '297.8 	104.6 	317.0 	159.5 	155.4 	576.4 	280.5 	194.4 	503.2 	121.2 	116.5 	14.5'.split()
# d_5 = '333.5 	125.5 	292.0 	215.0 	176.5 	350.5 	20.0 	81.0 	400.5 	63.5 	148.0 	13.0'.split()
a_5 = '441.2 	422.2 	317.1 	192.9 	176.2 	255.0 	125.3 	112.3 	531.7 	814.9 	313.0 	139.6'.split()
a_6 = '254.7 	264.5 	288.8 	141.9 	229.1 	824.9 	67.9 	20.2 	188.8 	409.8 	708.2 	458.8'.split()
a_7 = '541.7 	360.5 	69.4 	108.7 	52.0 	244.5 	135.8 	92.0 	558.4 	403.5 	261.2 	578.0'.split()
a_8 = '382.1 	292.4 	209.1 	140.0 	404.2 	431.1 	102.3 	173.3 	659.1 	152.3 	219.0 	352.6'.split()
a_9 = '189.0 	161.7 	202.7 	223.8 	475.7 	91.7 	134.0 	212.0 	485.4 	505.0 	277.5 	936.5'.split()
a_all = [a_5, a_6, a_7, a_8, a_9]
new_a_all = {}
new_2 = {}
new = {}
number = int(5)
mouth = ["January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
for i in a_all:
    new = {}
    for i_2 in range(0, 12):
        new.update({mouth[i_2] : i[i_2]})
    new_2.update({"10"+str(number): new})
    number = number + 1
print(new_2)
a_all = {'a_5':a_5, 'a_6':a_6, 'a_7':a_7,'a_8':a_8,"a_9":a_9}
print(a_all)
# i = 1
# year = ['105','106','107','108','109']
# data = []
# all_data = {}
# for i in range(0,5):
#     all_data.update({year[i]:a_all[i]})
# print(all_data)

