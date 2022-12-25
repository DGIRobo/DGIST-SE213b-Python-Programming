# 성적정리 (사전 사용)

'''
Description

참고: 일반적으로 프로그래밍을 할 때, 특정한 방법을 사용하는 것을 강제하지는 않습니다. 그렇지만, 실습 시간 때는 이론 시간에 배운 내용을 익히도록 특정한 문법을 사용하도록 할 수 있습니다.
디지스트 2학년 학생들의 공통필수 교과들의 중간고사 점수를 정리하고자 한다. 아래와 같이, 공통필수 교과목들의 이름은 course_titles라는 리스트에, 그리고 중간고사 성적은 midterm_scores라는 사전에 주어져 있다.
midterm_scores는 아래와 같이 구성되어 있다.

학생이름과 course_titles에 주어진 순서대로의 중간고사 성적이 저장된 리스트를 저장하는 리스트가 한 학생의 이름과 중간고사 성적을 나타냄
위와 같은 리스트를을 원소로 가지는 리스트가 midterm_scores이다.
아래와 같은 예에서, Alice와 Victor의 중간고사 성적은 아래와 같다.

Alice의 선형대수, 세포와 생명현상, 프로그래밍 중간고사 점수는 각각 62, 60, 77
Victor의 선형대수, 세포와 생명현상, 프로그래밍 중간고사 점수는 각각 82, 67, 94

course_titles = ['Linear Algebra', 'Cell Biology', 'Programming']
midterm_scores = {
    'Alice': [62, 60, 77],
    'Bob': [84, 88, 87],
    'Carol': [88, 88, 97],
    'Chuck': [92, 71, 93],
    'Craig': [81, 89, 72],
    'Dan': [79, 100, 97],
    'Erin': [76, 72, 65],
    'Eve': [69, 84, 67],
    'Faythe': [66, 60, 70],
    'Frank': [88, 76, 64],
    'Grace': [66, 77, 92],
    'Heidi': [93, 93, 82],
    'Mallory': [77, 89, 82],
    'Oscar': [67, 63, 67],
    'Peggy': [70, 81, 86],
    'Sybil': [96, 94, 62],
    'Trent': [67, 66, 61],
    'Trudy': [85, 74, 90],
    'Victor': [82, 67, 94],
    'Walter': [67, 84, 86],
    'Wendy': [97, 92, 66]
}


print_scores(test_scores, course_titles, student_name)

함수동작
학생의 이름이 test_scores에 전달된 인자에 없는 경우: 학생이름이 없다고 출력을 한다, student_name이 'Emma'인 경우,
'There is no student named Emma.' 를 출력한다.
학생의 이름이 test_scores에 전달된 인자에 있는 경우: 학생들의 이름, 각 과목별 점수, 평균을 출력한다. 자세한 출력 형식은 아래 함수 사용 예시를 참고할 것 (평균: 소수점이하 1자리로 표시)

매개변수
test_scores: 키(key)가 학생들의 이름, 값(value)이 각 과목들의 점수를 포함하는 리스트인 사전
course_titles: 과목명(문자열)들이 저장된 리스트
student_name: 학생의 이름이 저장된 문자열

반환값
없음
'''

'''
함수사용예시

print_scores(midterm_scores, course_titles, 'Alice')
print_scores(midterm_scores, course_titles, 'Oscar')
print_scores(midterm_scores, course_titles, 'Emma')
'''

'''
실행 결과

Alice:
    Linear Algebra: 62
    Cell Biology: 60
    Programming: 77
    Average: 66.3
Oscar:
    Linear Algebra: 67
    Cell Biology: 63
    Programming: 67
    Average: 65.7
There is no student named Emma.
'''

# Code
def print_scores(test_scores, course_titles, student_name):
    """Print scores for a certain student"""
    Isin = test_scores.get(student_name, 0)
    if type(Isin) == list:
        sum = 0
        students_score = student_name + ':'
        for i in range(len(course_titles)):
            students_score = students_score + '\n    ' + course_titles[i] + ': ' + '%s' % Isin[i]
            sum+=Isin[i]
        Average = sum/len(Isin)
        students_score = students_score + '\n    Average: ' + '%.1f' % Average
        print(students_score)

    else: print('There is no student named ' + student_name + '.')

course_titles = ['Linear Algebra', 'Cell Biology', 'Programming']
midterm_scores = {
    'Alice': [62, 60, 77],
    'Bob': [84, 88, 87],
    'Carol': [88, 88, 97],
    'Chuck': [92, 71, 93],
    'Craig': [81, 89, 72],
    'Dan': [79, 100, 97],
    'Erin': [76, 72, 65],
    'Eve': [69, 84, 67],
    'Faythe': [66, 60, 70],
    'Frank': [88, 76, 64],
    'Grace': [66, 77, 92],
    'Heidi': [93, 93, 82],
    'Mallory': [77, 89, 82],
    'Oscar': [67, 63, 67],
    'Peggy': [70, 81, 86],
    'Sybil': [96, 94, 62],
    'Trent': [67, 66, 61],
    'Trudy': [85, 74, 90],
    'Victor': [82, 67, 94],
    'Walter': [67, 84, 86],
    'Wendy': [97, 92, 66]
}

print_scores(midterm_scores, course_titles, 'Alice')
print_scores(midterm_scores, course_titles, 'Oscar')
print_scores(midterm_scores, course_titles, 'Emma')
