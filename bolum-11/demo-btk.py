import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"

headerParams = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

response = requests.get(url, headers=headerParams)

html = BeautifulSoup(response.text, "html.parser")

kurslar = html.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper")

with open("kurslar.csv","w",encoding="utf-8") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["link","image","title","seviye","like","ogrenci"])

    for kurs in kurslar:
        anchor = kurs.a
        link = anchor.get("href")
        image = anchor.img.get("src")
        title = anchor.find(class_="font-medium text-base").string
        seviye = anchor.find(class_="txt-secondary font-medium").string

        sayilar = anchor.next_sibling.next_sibling.get_text(separator="-").split("-")
        like = sayilar[0]
        ogrenci = sayilar[1]

        csv_writer.writerow([link, image, title, seviye, like, ogrenci])
