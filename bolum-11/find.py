from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.div
sonuc = obj.find("div")
sonuc = obj.find("div")
sonuc = obj.find_all("div")
sonuc = len(obj.find_all("div"))
sonuc = obj.find_all("div")[1].h2
sonuc = obj.find_all("div")[1].ul
sonuc = obj.find_all("div")[1].ul.find_all("li")
sonuc = obj.find_all("div")[1].ul.find_all("li")[2]
sonuc = obj.find_all("div")[1].ul.find_all("li")[2].string

for div in obj.find_all("div"):
    if div.h2.a != None:
        print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())

for a in obj.find_all("a"):
    print(a)

