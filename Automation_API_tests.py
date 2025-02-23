import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print("Status code :" + str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Excelent")
else:
    print("Status code is wrong")
result.encoding = 'utf-8'
print(result.text)