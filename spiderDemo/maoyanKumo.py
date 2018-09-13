import requests
import threading
import re
import os

class Kumo(threading.Thread):

    def __init__(self, size=10, offset=0, *args, **kwargs):
        super(Kumo, self).__init__(*args, **kwargs)
        self.__size = size
        self.__offset = offset

    def __analysis(self, text):
        pattern = (
            r'<dd>.*?'
            r'<i.*?>(.*?)</i>.*?'
            r'<a.*?title="(.*?)".*?>.*?'
            r'<img.*?data-src="(.*?)".*?/>.*?'
            r'<p.*?class="star".*?>(.*?)</p>.*?'
            r'(<i.*?class="integer".*?>(.*?)</i>.*?)?'
            r'(<i.*?class="fraction".*?>(.*?)</i>.*?)?'
            r'</dd>'
        )
        regex = re.compile(pattern, re.S)
        list = re.findall(regex, text)
        return list

    def __getRequest(self):
        path = 'http://maoyan.com/board/4'
        params = {
            'offset': self.__offset,
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '__mta=121018807.1536826550764.1536830236040.1536830276670.21; uuid_n_v=v1; uuid=38E408C0B72D11E89A858DEEF74451836BE8D0EA2D0445A1A09C5D0CCC397259; _csrf=288be9a765aca59fc9922f35f640e513067cdd1e671db7569cdbde5e7e038c1a; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=165d200276445-0e14ab42882e82-182e1503-1aeaa0-165d2002765c8; _lxsdk=38E408C0B72D11E89A858DEEF74451836BE8D0EA2D0445A1A09C5D0CCC397259; __mta=121018807.1536826550764.1536826554858.1536826565199.3; _lxsdk_s=165d2386573-c4b-43b-5cc%7C%7C4',
            'Host': 'maoyan.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
        reponse = requests.get(url=path, params=params, headers=headers)
        return reponse.text

    def __save(self, item, file):
        text = item[0].strip()+','
        text += item[1].strip()+','
        text += item[2].strip()+','
        text += item[3].strip()+','
        text += item[5].strip()+','
        text += item[7].strip()+'\n'
        file.write(text)

    def run(self):
        html = self.__getRequest()
        list = self.__analysis(html)
        if not os.path.exists('data'):
            os.mkdir('data')
        file = open('data/maoyan.csv', 'a+')
        for item in list:
            self.__save(item, file)
        file.close()


if __name__ == '__main__':
    list = []
    for i in range(0, 100, 10):
        k = Kumo(offset=i)
        list.append(k)
    for i in list:
        i.start()
        #i.join()