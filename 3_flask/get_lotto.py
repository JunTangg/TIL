import requests
import json


num = input('num: ')
lotto_nb = []


def return_lotto_number(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    data = requests.get(url).text
    lotto_data = json.loads(data)
    lotto_nb.append([lotto_data['drwtNo1'], lotto_data['drwtNo2'], lotto_data['drwtNo3'], lotto_data['drwtNo4'], lotto_data['drwtNo5'], lotto_data['drwtNo6']])
    return lotto_nb


price_num = return_lotto_number(num)
print(price_num)
