from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.div
sonuc = obj.find("div")
sonuc = obj.find(id="item1")
sonuc = obj.find(id="item2")
sonuc = obj.find(id="header")
sonuc = obj.find(class_="item")
sonuc = obj.find_all(class_="item")
sonuc = obj.find_all(class_="item")[1]

sonuc = obj.select("#header")
sonuc = obj.select("#item1")
sonuc = obj.select(".item")

sonuc = obj.select_one(".item")
sonuc = obj.select_one("#item1")

sonuc = obj.div.attrs["id"]
sonuc = obj.div.attrs["class"]

sonuc = obj.ul.get_text(strip=True, separator="-")

for a in obj.div.find_all("a"):
    # print(a.get("href"))
    print(a["href"])



print(sonuc)