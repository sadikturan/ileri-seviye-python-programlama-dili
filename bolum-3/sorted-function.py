sayilar = [1,53,4,5,65,23]

# sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)

users = [
    {"username":"sadikturan", "posts": ["post 1", "post 2"],"email":"info@abc.com","phone":"1234"},
    {"username":"ahmetyilmaz", "posts": ["post 1"],"email":"info@abcd.com"},
    {"username":"cananyilmaz", "posts": ["post 1", "post 2", "post 3"]}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda user: len(user["posts"]))
sonuc = sorted(users, key=lambda user: len(user["posts"]), reverse=True)

sonuc = list(map(lambda user: user["username"],sorted(users, key=lambda user: len(user["posts"]))))

kurslar = [
    {"title":"python","count":10000},
    {"title":"web geliştirme","count":20000},
    {"title":"javascript","count":5000},
]

sonuc = sorted(kurslar, key= lambda kurs: kurs["count"])
sonuc = sorted(kurslar, key= lambda kurs: kurs["count"], reverse=True)
sonuc = list(map(lambda kurs: kurs["title"], sorted(kurslar, key= lambda kurs: kurs["count"], reverse=True)))

print(sonuc)