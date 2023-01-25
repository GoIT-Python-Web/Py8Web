import re
import json
from typing import List
from datetime import datetime

import requests
from bs4 import BeautifulSoup

base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_urls() -> List[str]:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.select('div[class=ajaxmonth] h4 a')
    urls = ["/"]
    prefix = "/month.php?month="
    for link in content:
        urls.append(prefix + re.search(r"\d{4}-\d{2}", link["href"]).group())

    return urls


def spider(urls: List[str]):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.select('ul[class=see-also] li[class=gold]')

        for element in content:
            result = {}
            date = element.find('span', attrs={"class": "black"}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f'Error for {date}')
                continue

            result.update({"date": date})
            losses = element.find('div').find('div').find('ul')
            for l in losses:
                title, quantity, *rest = l.text.split("—")
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()
                result.update({title: int(quantity)})

            data.append(result)
    return data


if __name__ == '__main__':
    urls = get_urls()
    # print(urls)
    result = spider(urls)
    print(result)
    with open('losses.json', "w", encoding="utf-8") as fd:
        json.dump(result, fd, ensure_ascii=False)
