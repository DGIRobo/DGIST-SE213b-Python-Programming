# DGIST 홈페이지 내 URL 찾기

'''
Description

DGIST 홈페이지에서 e-mail 주소와 dgist.ac.kr/로 시작되는 모든 url을 가져오는 함수를 작성하시오.
e-mail 주소는 앞의 문제에서 풀었던 코드를 그대로 가져와서 getEmailAddr(txt)로 사용하고,
여기서는 getURL(txt)를 작성하시오.


getURL(txt) 함수

매개변수
txt: dgist.ac.kr 홈페이지의 첫 페이지의 문자열

반환값:
dgist.ac.kr/로 시작되는 모든 url
dgist.ac.kr/ 이하는 /, _, . 과 숫자, 문자로 이루어져 있음

함수의 동작
txt문자열에 포함되어 있는 dgist.ac.kr/ 로 시작되는 모든 url주소를 리스트로 반환
'''

'''
함수 사용예시

with urlopen("https://www.dgist.ac.kr/kr/") as u :
    dgist = u.read().decode("utf-8")
print(getEmailAddr(dgist))
print(getURL(dgist))
'''

'''
실행결과

['webmaster@dgist.ac.kr', 'webmaster@dgist.ac.kr']
['dgist.ac.kr/common/img/common/og_img.png', 'dgist.ac.kr/kr/', 'dgist.ac.kr/search.do', 'dgist.ac.kr/site/cyber/tour/', 'dgist.ac.kr/giving/', 'dgist.ac.kr/adm/', 'dgist.ac.kr/gadm/', 'dgist.ac.kr/iadm/', 'dgist.ac.kr/', 'dgist.ac.kr/home.do', 'dgist.ac.kr/ucs/ucsqProfRespSbjtInq/index.do', 'dgist.ac.kr/', 'dgist.ac.kr/', 'dgist.ac.kr/sub01/sub01.php', 'dgist.ac.kr/site/cyber/tour/', 'dgist.ac.kr/giving/', 'dgist.ac.kr/adm/', 'dgist.ac.kr/gadm/', 'dgist.ac.kr/iadm/', 'dgist.ac.kr/', 'dgist.ac.kr/home.do', 'dgist.ac.kr/ucs/ucsqProfRespSbjtInq/index.do', 'dgist.ac.kr/', 'dgist.ac.kr/', 'dgist.ac.kr/sub01/sub01.php', 'dgist.ac.kr/kr/html/sub06/060101.html', 'dgist.ac.kr/kr/html/sub06/060101.html', 'dgist.ac.kr/kr/html/sub06/060101.html', 'dgist.ac.kr/kr/html/sub06/060101.html', 'dgist.ac.kr/kr/html/sub06/060101.html', 'dgist.ac.kr/kr/html/sub05/050106.html', 'dgist.ac.kr/kr/html/sub05/050101.html', 'dgist.ac.kr/kr/html/sub05/050102.html', 'dgist.ac.kr/kr/html/sub05/050102.html', 'dgist.ac.kr/kr/html/sub05/050101.html', 'dgist.ac.kr/kr/html/sub05/050101.html', 'dgist.ac.kr/kr/html/sub05/050101.html', 'dgist.ac.kr/kr/html/sub05/050101.html', 'dgist.ac.kr/kr/html/sub05/050104.html', 'dgist.ac.kr/kr/html/sub05/050104.html', 'dgist.ac.kr/kr/html/sub05/050104.html', 'dgist.ac.kr/kr/html/sub05/050104.html', 'dgist.ac.kr/kr/html/sub05/050108.html', 'dgist.ac.kr/kr/html/sub05/050108.html', 'dgist.ac.kr/kr/html/sub05/050108.html', 'dgist.ac.kr/kr/html/sub05/050108.html', 'dgist.ac.kr/kr/html/sub05/050106.html', 'dgist.ac.kr/kr/html/sub05/050106.html', 'dgist.ac.kr/kr/html/sub05/050106.html', 'dgist.ac.kr/kr/html/sub05/050106.html', 'dgist.ac.kr/index.html', 'dgist.ac.kr/', 'dgist.ac.kr/site/dgist_library/menu/747.do', 'dgist.ac.kr/home
'''

# Codes
from urllib.request import urlopen
import re

def getEmailAddr(txt):
    """return the list of e-mails from the txt"""
    emails = re.findall('[a-zA-Z0-9]{1,}@[a-z]{1,}[.]{1}[a-z.]{1,}', txt)
    return emails

def getURL(txt):
    """return the list of urls starting with 'dgist.ac.kr/' from the txt"""
    URLs = re.findall('dgist.ac.kr/[ /_.a-zA-Z0-9]{0,}', txt)
    return URLs

if __name__ == '__main__':
    with urlopen("https://www.dgist.ac.kr/kr/") as u :
        dgist = u.read().decode("utf-8")
    print(getEmailAddr(dgist))
    print(getURL(dgist))
