# 이미지에서 숫자 판별

'''
Description

32x32 픽셀을 갖는 bmp파일의 이름을 인자로 받아서 숫자 1인지 0인지를 판별하는 함수를 작성하시오.

(week7의 48번 문제를 참조해서 풀면 됩니다.

주의: 이미지에는 숫자 1 또는 0 숫자 한 개만 들어있으며, 아래와 같은 손글씨, 또는 컴퓨터 폰트로 저장되어있다.

Tip: byte string으로 읽어 들인 파일의 값에서 1바이트를 가져오면 int로 해석이 됨.
즉, b'\x00\xff\x00'[1] == 255 와 같음.
이미지를 다음과 같이 가정함. 바탕은 255(b'\xff' : 흰색)로 되어 있고 글자는 0(b'\x00': 검정)으로 되어 있음.
데이터를 중간중간 print해보고 값을 보면서 디버깅을 하면 도움이 됨.
'''

'''
함수 read_img(img_name)

함수동작
파일 이름(img_name)을 매개변수로 받아서 0 또는 1일 들어있는 파일을 열어보고 이미지에 있는 숫자를 반환함

매개변수
img_name (str) 숫자가 저장되어 있는 bmp 파일이름

반환값
(int) 이미지에 쓰여진 0 또는 1을 판별하여 반환
'''

'''
실행 예시

print( read_img("img0.bmp") )
print( read_img("img1.bmp") )
'''

'''
실행 결과

0
1
'''

#Code
def read_img(img_name):
    with open(img_name, "rb") as f:
        data = f.read()
        img = data[-512:]
        imgList = []
        reverseNums = [[]]
        for i in range(len(img)):
            '''
            print('%3s' % img[i], end=' ')
            if (i+1)%16 == 0:
                print('')
            '''
            if i%16 == 0:
                imgList.append(list())
            imgList[int(i/16)].append(img[i])
        for j in range(len(imgList)):
            candidate = []
            for k in range(15):
                if imgList[j][k]!=imgList[j][k+1]:
                    candidate.append(1)
            reverseNums.append(candidate)
    if reverseNums[int(len(reverseNums)/2)] == [1,1]:
        return 1
    if reverseNums[int(len(reverseNums)/2)] == [1,1,1,1]:
        return 0

if __name__ == '__main__':
    print( read_img("img0.bmp") )
    print( read_img("img1.bmp") )
    print( read_img("img2.bmp") )
    print( read_img("img3.bmp") )
    print( read_img("img4.bmp") )
