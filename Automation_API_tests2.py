import requests


class RandomTest():
    """Checking"""

    def __int__(self):
        pass

    def random_test(self):
        """Create Random"""

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
    check = result.json()
    check_info = check.get("categories")
    print(check_info)
    assert check_info == []
    print("Right categories")
    check_info_value = check.get("value")
    print(check_info_value)
    name = "Chuck"
    if name in check_info_value:
        print("The name is " + name + " exist")
    else:
        print("The name is  " + name + " not exist")


random = RandomTest()
random.random_test()
