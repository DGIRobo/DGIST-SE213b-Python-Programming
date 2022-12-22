# Url / regular expression 사용

'''
Description
test 페이지에서 원하는 값을 가져오는 방법
'''

# Codes
from urllib.request import urlopen
import re

with urlopen('http://10.180.2.80/test.html') as f:
    txt = f.read() # return byte string

print(txt)
print(txt.decode('utf-8'))

for sentence in txt.decode('utf-8').splitlines():
    print(sentence)
    if sentence.startswith('Contact: ') :
         phone = sentence[9:]
print(phone)

with urlopen('http://10.180.2.80/test.html') as f:
    txt = f.read().decode('utf-8')
print(re.findall("[가-힣]+", txt))
print(re.findall("날씨[ ]*:[ ]*[가-힣]+", txt))
print(re.findall("날씨[ ]*:[ ]*([가-힣]+)", txt))
print(re.findall("([가-힣]+)[ ]*:[ ]*([가-힣]+)", txt))
