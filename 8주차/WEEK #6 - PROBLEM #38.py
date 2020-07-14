# 문자열 변환

'''
Description

아이템과 해당 아이템의 가격이 미국 달러로 주어진 문장을 대한민국 통화인 원으로 변경해 주는 함수 change_currency()를 구현하시오.

주의 다양한 문자열 함수를 이용

Hint

함수동작
미국 달러로 적혀있는 아이템의 가격을 현재 환율(rate)에 맞춰서 대한민국 원화로 변경후 변경된 문자열을 반환하는 함수
매개변수
sentence: (문자열) 아이템과 가격(US달러로)이 줄바꿈기호로 나누어져 저장된 문자열
   - 문자열은 모두 다음 형식으로 작성된
   - item : cost currency
   - (i.e. Apple : 1 USD)
rate:(float) 현재 1달러가 몇 원인지 알려주는 실수 값
반환값
(문자열) 아이템과 주어진 가격을 원화로 변경한 결과를 줄바꿈기호를 이용하여 하나의 문자열로 반환
'''

'''
함수 사용 예시

menu = """Apple : 1.5 USD
Banana : 1 USD
Cake : 12 USD
"""
usd = 1200.0 # 1usd = 1200kwn
result = change_currency(menu, usd)
print(result)
'''

'''
실행결과

Apple : 1800.0 KWN
Banana : 1200.0 KWN
Cake : 14400.0 KWN
'''

# Code
def change_currency(sentence, rate):
    korean_list=[]
    word_list = sentence.splitlines()
    for word in word_list:
        item, colon, usd_price, country = word.split(' ')
        kwn_price = float(usd_price)*rate
        korean_list.append([item, kwn_price])
    korean_menu=''
    for word in korean_list:
        korean_menu = korean_menu + word[0] + ' : ' + '%s' % word[1] + ' KWN'
        if word == korean_list[-1]: break
        korean_menu = korean_menu + '\n'
    return korean_menu


menu = """Apple : 1.5 USD
Banana : 1 USD
Cake : 12 USD
"""

usd = 1200.0 # 1usd = 1200kwn
result = change_currency(menu, usd)
print(result)
