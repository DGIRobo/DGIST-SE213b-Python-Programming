'''
Description
사용자에게 반지름의 길이를 입력 받아 그 반지름의 길이를 가지는 구의 부피와 겉넓이를 출력할
것. pi의 값은 3.141592 또는 그에 근접한 값으로 설정할 수 있다. 첫 번째 줄 마지막에는 구의 부피
가, 두번째 줄 마지막에는 구의 겉넓이가 출력되어야 하며 공백으로 구분되어야 한다.
'''

'''
실행예시
Enter the radius of a sphere: 12.3
The volume of the sphere: 7794.779840352002
The surface area of the sphere: 1901.1658147200003
'''

radius = float(input('Enter the radius of a sphere: '))
volume = (4/3)*(3.141592)*(radius)*(radius)*(radius)
surface = 4*(3.141592)*(radius)*(radius)
print('The volume of the sphere: ',volume)
print('The surface area of the sphere: ', surface)