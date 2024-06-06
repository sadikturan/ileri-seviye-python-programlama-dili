import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "<api_key>"

konum = input("konum: ")

response = requests.get(url, params= {
    "key" : key,
    "q" : konum,
    "lang": "tr"
})

sonuc = response.json()
sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havadurumu} derece ve {text}")