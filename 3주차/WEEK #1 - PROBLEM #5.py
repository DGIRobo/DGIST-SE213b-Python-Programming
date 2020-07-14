'''
Description
사용자에게 두 물체의 질량과 거리를 입력받아, 만유인력에 의해 가해지는 힘을 계산하는 프로그
램을 작성할 것. 만유인력의 공식과 중력상수 G의 값은 아래와 같다.
'''

'''
실행예시
Enter the mass of object 1 (kg): 5.972e24
Enter the mass of object 2 (kg): 1.989e30
Enter the distance between object 1 and object 2 (m): 1.496e11
The force between the object 1 and object 2 is 3.5421519355858043e+22 N
'''

mass1 = float(input('Enter the mass of object 1  (kg) : '))
mass2 = float(input('\nEnter the mass of object 2  (kg) : '))
distance = float(input('\nEnter the distance between object 1 and object 2 (m) : '))
force = (6.67384e-11)*(mass1*mass2)/(distance*distance)
print('The force between the object 1 and object 2 is' , force , 'N')