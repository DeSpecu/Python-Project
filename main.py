from lxml import html
import requests

def list_to_string(s):
    news = ""
    for x in s:
        news += x
    return news

def request():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}
    html_file = requests.get("https://www.x-kom.pl", headers=headers)
    tree = html.fromstring(html_file.content)

    cenastara = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[1]/span[1]/text()')
    cenanowa = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[1]/span[2]/text()')
    oszczednosc = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[2]/p/text()')
    ilosc = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/p/text()')
    co = tree.xpath('//*[@id="hotShot"]/div/a/div/div[1]/div/span/img/@alt')
    
    result = (f"Gorący Strzał teraz:\n{list_to_string(co)}\nStara cena: {list_to_string(cenastara)}\n"
    f"Nowa cena: {list_to_string(cenanowa)}\n{list_to_string(oszczednosc)}\nZostało sztuk: {list_to_string(ilosc)}")

    return result

print(request())