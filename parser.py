import bs4
import requests
from data import base_url, DESIRED_HUBS

DESIRED_HUBS = list(map(str.lower, DESIRED_HUBS))


def parser():
    HEADERS = {
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"8c1f8437f8acfee6e4ef83eafd4db112"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                      'Safari/537.36',
        'sec-ch-ua-mobile': '?0'
    }

    ret = requests.get(base_url, headers=HEADERS)
    text = ret.text
    soup = bs4.BeautifulSoup(text, features='html.parser')

    posts = soup.find_all('article')
    for post in posts:
        habs = post.find_all(class_='tm-article-snippet__hubs-item')
        habs = [hab.text.strip() for hab in habs]
        habs = list(map(str.lower, habs))
        a = set(DESIRED_HUBS)
        b = set(habs)
        z = a.isdisjoint(b)
        if not z:
            data = post.find('time').attrs['title']
            href = post.find(class_="tm-article-snippet__title-link").attrs["href"]
            title = post.find('h2').find('span').text
            conclusion = f"{data}\n{title} - {base_url}{href}"
            print(conclusion,'\n')


if __name__ == '__main__':
    parser()
