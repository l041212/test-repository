from urllib import request
from urllib import parse
from urllib import error
import json
import pymongo
import requests
import threading

TEXT = ['数据分析']
CITY = ['深圳']
database = None

def getPageReponse(pn, text, city):
    path = 'https://www.lagou.com/jobs/positionAjax.json?'
    path += 'city='+parse.quote(city)+'&'
    path += 'needAddtionalResult=false'
    paramters = {
        'first': 'true',
        'pn': pn,
        'kd': text,
    }
    headerData = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': 55,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'WEBTJ-ID=20180912113413-165cbd7fb1d376-0c09e6aa6cbd4e-182e1503-1764000-165cbd7fb1e15c; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536723254; _ga=GA1.2.1582848340.1536723254; _gid=GA1.2.727085021.1536723254; _gat=1; user_trace_token=20180912113414-b8888e33-b63c-11e8-9583-525400f775ce; LGSID=20180912113414-b8888fc2-b63c-11e8-9583-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3Dlagou; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180912113414-b8889156-b63c-11e8-9583-525400f775ce; JSESSIONID=ABAAABAAAGFABEF269C919D151413F34068E4F033446FE2; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536723300; LGRID=20180912113500-d3beeba1-b63c-11e8-9583-525400f775ce; SEARCH_ID=dac5fbcd5d0b4f4f8d596ace190d01df',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_'+parse.quote(text)+'?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    paramterData=bytes(parse.urlencode({'first': 'true','pn': pn,'kd': '数据分析'}), encoding='utf8')
    requestObject = request.Request(url=path, data=paramterData, headers=headerData, method='POST')
    response = request.urlopen(requestObject)
    return json.loads(response.read().decode('utf8'))

def getPageData(pn, text, city):
    print(str(pn)+'++++++++++++')
    set = getPageReponse(pn, text, city)
    for element in set['content']['positionResult']['result']:
        parameters = {
            'companyId': element['companyId'],
            'companyShortName': element['companyShortName'],
            'education': element['education'],
            'positionName': element['positionName'],
            'salary': element['salary'],
            'workYear': element['workYear'],
            'companyFullName': element['companyFullName'],
        }
        savePageItemData(parameters)
    return None

def savePageItemData(item):
    global database
    if database != None:
        collection = database.lagou
        print(item)
        collection.update({'companyId': item['companyId']}, {'$set': item}, True)

def execute():
    global client
    global database
    client = pymongo.MongoClient('localhost', 27017)
    database = client['test']
    first = getPageReponse(1, TEXT[0], CITY[0])
    totalCount = first['content']['positionResult']['totalCount']
    for i in range(1, totalCount//15+2):
        getPageData(i, TEXT[0], CITY[0])

class KumoBeta(threading.Thread):

    def __init__(self, text=None, city=None, database=None, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.text = text
        self.city = city
        self.path = 'https://www.lagou.com/jobs/positionAjax.json'
        self.database = database

    def __getData(self, pn):
        params = {
            'city': self.city,
            'needAddtionalResult': 'false',
        }
        data = {
            'first': 'true',
            'pn': pn,
            'kd': self.text,
        }
        headers = {
            'Accept': 'application/json,text/javascript,*/*;q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'WEBTJ-ID=20180912113413-165cbd7fb1d376-0c09e6aa6cbd4e-182e1503-1764000-165cbd7fb1e15c; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536723254; _ga=GA1.2.1582848340.1536723254; _gid=GA1.2.727085021.1536723254; _gat=1; user_trace_token=20180912113414-b8888e33-b63c-11e8-9583-525400f775ce; LGSID=20180912113414-b8888fc2-b63c-11e8-9583-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3Dlagou; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180912113414-b8889156-b63c-11e8-9583-525400f775ce; JSESSIONID=ABAAABAAAGFABEF269C919D151413F34068E4F033446FE2; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536723300; LGRID=20180912113500-d3beeba1-b63c-11e8-9583-525400f775ce; SEARCH_ID=dac5fbcd5d0b4f4f8d596ace190d01df',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_' + parse.quote(self.text) + '?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
        response = requests.post(url=self.path, params=params, data=data, headers=headers)
        return response.json()

    def __savePage(self, item):
        if self.database != None:
            collection = self.database.lagou
            collection.update({'companyId': item['companyId']}, {'$set': item}, True)

    def __getPage(self, pn):
        print(str(pn) + '++++++++++++')
        set = self.__getData(pn)
        for element in set['content']['positionResult']['result']:
            parameters = {
                'companyId': element['companyId'],
                'companyShortName': element['companyShortName'],
                'education': element['education'],
                'positionName': element['positionName'],
                'salary': element['salary'],
                'workYear': element['workYear'],
                'city': element['city'],
                'companyFullName': element['companyFullName'],
            }
            #print(parameters['city']+':'+parameters['companyFullName'])
            self.__savePage(parameters)
        return None

    def run(self):
        first = self.__getData(1)
        totalCount = first['content']['positionResult']['totalCount']
        for i in range(1, totalCount // 15 + 2):
            self.__getPage(i)

if __name__ == '__main__':
    text = ['数据分析','爬虫']
    city = ['广州', '深圳','北京']
    kumos = []
    client = pymongo.MongoClient('localhost', 27017)
    database = client['test']
    for txt in text:
        for cty in city:
            kumo = KumoBeta(txt, cty, database)
            kumos.append(kumo)
    for kumo in kumos:
        kumo.start()