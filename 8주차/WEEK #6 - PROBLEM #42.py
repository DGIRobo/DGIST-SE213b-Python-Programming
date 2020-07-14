# 문자열 서식

'''
Description

String Formatting
'''

# Code

n = 42
f = 42.195
s = 'string cheese'
pi = 3.1415926535897932384626433832795028841971693

# 기본 사용. fieldname을 생략하면 순서대로 인자 사용
print('{} {} {}'.format(n, f, s))
# {} 이외의 부분은 문자열 그대로
print('The first argument is {}'.format(n))

print('{2} {0} {1}'.format(n, f, s)) # 인자 순서를 숫자로 지정
print('{0} is {0}'.format(n))        # 같은 인자를 여러 번 사용
# 이름을 이용해 인자지정
print('{integer} {realnumber} {string}'.format(integer=n,
                                               realnumber=f,
                                               string=s))
# 인자의 자료형 지정
# d: 정수, f: 실수, s: 문자열
# g: general format. 아주 크거나 작으면 지수로 표현
#    아니면 실수로 표현, 단 소수점 이하의 0은 생략
print('{:d} {:f} {:s}'.format(n, f, s))
print('{0:d} {0:f} {0:g}'.format(n))  # 정수를 실수로는 변환 가능
print('{0:f} {0:g}'.format(f))        # g를 사용하면 조금 더 보기편한 숫자를 표시함
#print('{0:d}'.format(f))              # 실수를 정수로 바꾸려고 하면 에러 발생

print('-' * 10)
print('{:10d}'.format(n))    # 10칸에 맞추어 출력
print('{:>10d}'.format(n))   # 오른쪽 정렬
print('{:<10d}'.format(n))   # 왼쪽 정렬
print('{:^10d}'.format(n))   # 가운데 정렬
print('{:.>10d}'.format(n))  # 빈 칸 대신 . 사용
print('{:_<10d}'.format(n))  # 빈 칸 대신 _ 사용
print('{:*>10d}'.format(n))  # 빈 칸 대신 * 사용
print('{:10.3f}'.format(pi)) # 소수점 이하 정밀값
print('{:10.5s}'.format(s))  # 문자열 중 몇 글자만 출력

print('{:10.3f}'.format(pi)) # 소수점 이하 정밀값
print(f'{pi:10f}')
print(f'{pi:10g}')
print(f'{0.0003145:10g}')
print(f'{0.00003145:10g}')
print(f'{123456:10g}')
print(f'{123456789:10g}')
# 실수 반올림
