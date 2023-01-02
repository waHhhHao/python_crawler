import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/'
    response = requests.get(url)  # HTML源码数据
    text = response.text
    print(text)
    with open('./sogou.html', 'w', encoding='utf-8') as f:
        f.write(text)
