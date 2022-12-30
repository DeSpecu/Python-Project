from lxml import html
import requests
import datetime

path = "C://Users//szymk//Desktop//Strzaly.txt"

def list_to_string(s):
    news = ""
    for x in s:
        news += x
    return news

def find(find_it):
    file_to_search = open(path)
    read = file_to_search.read()
    index = read.find(find_it)
    if index>-1:
        return True
    return False

def save(dane):
    file_to_save = open(path, 'a+')
    dane = dane[0:dane.find("Zostało"):]
    file_to_save.write(f"{dane}\n")
    print("Zapisano!")

def previous(to_find):
    file_search = open(path)
    lines = file_search.readlines()
    for x in range(len(lines)):
        if to_find in lines[x]:
            return lines[x:x+4]

def ask():
    answear = input("Czy chcesz wyszukać wcześniejszy strzał? y/n\n")
    if answear == 'y':
        day = input("Podaj dzień\n")
        month = input("Podaj miesiąc\n")
        year = input("Podaj rok\n")
        hour = input("Godzina 10 czy 22?\n")
        while hour != '10' and hour != '22':
            print("Podaj godzinę 10 lub 22")
            hour = input()

        result = previous(f"{day}-{month}-{year} Godzina: {hour}")
        if result is not None:
            print(f"Promocja z tej daty:\n{list_to_string(result)}")
        else:
            print("Nie znaleziono!\n")

def request():
    date = datetime.datetime.now()
    if date.hour<22 and date.hour>9:
        date_string = f"{date.day}-{date.month}-{date.year} Godzina: 10"
    else:
        date_string = f"{date.day}-{date.month}-{date.year} Godzina: 22"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}
    html_file = requests.get("https://www.x-kom.pl", headers=headers)
    tree = html.fromstring(html_file.content)

    cenastara = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[1]/span[1]/text()')
    cenanowa = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[1]/span[2]/text()')
    oszczednosc = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/div[2]/p/text()')
    ilosc = tree.xpath('//*[@id="hotShot"]/div/a/div/div[2]/p/text()')
    co = tree.xpath('//*[@id="hotShot"]/div/a/div/div[1]/div/span/img/@alt')
    
    result = (f"Data: {date_string}\n{list_to_string(co)}\nStara cena: {list_to_string(cenastara)}\n"
    f"Nowa cena: {list_to_string(cenanowa)}\n{list_to_string(oszczednosc)}\nZostało sztuk: {list_to_string(ilosc)}")

    return result

output = request()
ask()

date = datetime.datetime.now()
if date.hour<22 and date.hour>9:
    date_string = f"{date.day}-{date.month}-{date.year} Godzina: 10"
    if not find(date_string):
        save(output)
else:
    date_string = f"{date.day}-{date.month}-{date.year} Godzina: 22"
    if not find(date_string):
        save(output)

print(output)