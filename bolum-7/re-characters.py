import re

text = "A343a 123 XYZ 456 @&% 300 2 A343a 123456 1_2 abc"

# pattern = r"\d\d\d"
# pattern = r"\d+"
# pattern = r"\d*"
# pattern = r"\d{3}"
# pattern = r"\d{3,5}"
# pattern = r"\d{3,}"
# pattern = r"\d{,5}"
# pattern = r"\d.\d"
# pattern = r"[a-zA-Z0-9]"
# pattern = r"\d|[a-z]"
# pattern = r"\d\w\w\w"
# pattern = r"^A\d\w\w\w"
pattern = r"A\d\w\w\w$"

# matches = re.search(pattern, text)
# matches = re.findall(pattern, text)
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())

