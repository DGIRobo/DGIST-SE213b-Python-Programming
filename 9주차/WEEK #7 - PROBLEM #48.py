# 이미지 파일 변형 (바이너리 파일 입출력)

'''
Description

이 파일이 위치한 디렉토리에 아래와 같은 비트맵 이미지 파일(original.bmp)이 있다. 이미지에 하트 모양이 표시되도록 이미지를 변경하시오.
'''

# Code (미완인 code임. -> 하트로 바꿔주는 부분만 추가하면 완성됨.)
with open("original.bmp", "rb") as f:
    data = f.read()

# print(len(data))
# print(data)
new_data = data[:-512]
new_data+=data[-512:].replace(b"\xff", b"\xff")

with open("original.bmp", "wb") as f:
    if len(new_data) == 630:
        f.write(new_data)
        print("end")
    else :
        print("file size error")
