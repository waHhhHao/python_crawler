import requests
import json

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    word = input('>>> ')
    data = {
        'kw': word
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }
    response = requests.post(url=url, data=data, headers=headers)
    text = response.json()
    fp = open('./baidu_translation_{word}.json', 'w', encoding='utf-8')
    json.dump(text, fp=fp, ensure_ascii=False)
