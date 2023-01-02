import requests

# 网页的反爬虫会检测UA，如果检测到是爬虫程序会拒绝访问
# 需要伪装
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    query = input('query:')

    params = {
        'query': query
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }

    response = requests.get(url, params, headers=headers)  # 此时User-Agent编程了爬虫
    text = response.text
    with open(f'./sogou_{query}.html', 'w', encoding='utf-8') as F:
        F.write(text)
