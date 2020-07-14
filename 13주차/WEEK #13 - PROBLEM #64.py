# 기상청 사이트에서 대구지역 내일 날씨 가져오기

'''
Description
기상청에서 제공하는 rss 로 부터 날짜와 지역을 넣어서 날씨를 가져오는 함수 getForecast(loc, day)를 작성하시오.


getForecast(loc, day) 함수

매개변수
loc: (문자열) 도시이름
day: (문자열) 2020-05-28 와 같은 형식

반환값:
기상 예보 (예: 맑음)

함수의 동작
기상예보에서 해당 날짜와 지역의 날씨를 가져와서 반환함
전국 기상 중기예보: https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
'''

'''
함수 사용예시

print(getForecast("대구", "2020-05-28")
'''

'''
실행결과

맑음
'''

# Codes
from urllib.request import urlopen
import re

def getForecast(loc, day):
    with urlopen('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108') as f:
        allTxt = f.read().decode('utf-8').splitlines()
        location_data = allTxt[allTxt.index('\t\t\t\t<city>'+loc+'</city>'):]
        if '\t\t\t\t\t<tmEf>'+day+' 12:00</tmEf>' in location_data:
            day_data = location_data[location_data.index('\t\t\t\t\t<tmEf>'+day+' 12:00</tmEf>'):]
        else:
            day_data = location_data[location_data.index('\t\t\t\t\t<tmEf>'+day+' 00:00</tmEf>'):]
        return day_data[1].strip('\t</wf>')

if __name__ == '__main__':
    print(getForecast("대구", "2020-05-28"))
