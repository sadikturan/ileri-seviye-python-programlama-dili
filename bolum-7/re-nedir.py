import re

text = "BTK Akademi Python Dersleri BTK"
pattern = "BTK"

match = re.search(pattern, text)

sonuc = match
sonuc = match.start()
sonuc = match.end()

match = re.findall(pattern, text)

sonuc = match


print(sonuc)
