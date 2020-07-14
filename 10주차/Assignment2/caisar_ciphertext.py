# 카이사르 암호

'''
일부 사람들만 이해할 수 있도록 정보를 저장하기 위한 방법을 암호화(encryption)라고 한다. 고대로부터 군사적인 목적으로 널리 사용되었고, 컴퓨터를 이용하여 정보를 안전하기 처리하기 위해서도 널리 사용된다. (https://seed.kisa.or.kr/kisa/intro/EgovHistory.do)
로마의 카이사르(Caesar)가 사용한 암호는 매우 간단한 규칙을 가지고 있다. 알파벳으로 구성된 문장을 암호화할 때는(encrypt) 미리 정해진 글자수만큼의 뒤의 알파벳으로 바꾸고, 암호문을 해독(혹은 복호화)할 때는 (decrypt) 역시 미리 정해진 글자수만큼의 앞의 알파벳으로 바꾼다.
예를 들어, 미리 정해진 글자수(암호키)가 3이라면, 'a' 는 'd'로 치환하고, 'b'는 'e'로 치환하는 방법으로 암호문을 만든다. 즉, 평문(plaintext) xyzabc를 암호화하면 암호문(ciphertext) abcdef가 된다.
카이사르 암호를 사용할 때, 한개의 평문과 암호문을 획득하면 암호키 값을 알 수 있다. 평문과 암호문을 입력 받아서 키 값을 리턴하는 함수 find_key()를 작성하고 찾은 키 값을 이용하여 주어진 암호문을 복호화 해주는 함수 decrypt() 함수를 아래와 같이 구현하시오.


find_key(plaintext, ciphertext)

함수동작
암호문(ciphertext)와 그 암호문을 만든 평문(plaintext)를 한쌍 획득하면,
카이사르 암호에서는 평문을 암호화 할때 사용한 key값을 찾을 수 있다.
key값을 찾아서 반환하는 함수

매개변수
plaintext: (문자열) 암호화 되지 않은 평문
plaintext에는 알파벳 소문자와 공백, 특수문자 등을 포함할 수 있다
ciphertext: (문자열) 특정 키를 통해 암호화(문자열 shift)된 암호문

반환값
(int) plaintext가 ciphertext로 변환될 때 사용된 글자수(암호키)


decrypt(ciphertext, key)

함수동작
암호문과 key값을 받아서 암호문을 해석하여 문자열을 반환

매개변수
ciphertext: (str) 암호화 되어있는 문자열
- ciphertext에는 알파벳 소문자와 공백, 특수문자 등을 포함할 수 있다.
key: (int) 평문을 암호화 할 때 사용한 키 값

반환값
암호문을 평문으로 변경한 문자열 반환
- ciphertext에 포함된 알파벳(소문자로만 이루어짐)은 key 글자 앞의 알파벳으로 변환 - ciphertext 중 알파벳이 아닌 글자들(문장부호, 빈칸 등)은 원래의 글자를 그대로 남
참고: 반환값은 ciphertext와 같은 글자수를 가진다


주의
if문을 26번 쓰지 말 것. 즉 알파벳별로 별도의 조건을 만들어서 처리하지 말 것.
'''

'''
함수사용예시
plain_text = 'hello, world'
cipher_text = 'khoor, zruog'
c1 = 'iluvw, vroyh wkh sureohp. wkhq, zulwh wkh frgh. - mrkq mrkqvrq'
c2 = 'zlwkrxw uhtxluhphqwv ru ghvljq, surjudpplqj lv wkh duw ri dgglqj exjv wr dq hpswb whaw iloh. - orxlv vubjohb'
c3 = 'frpsxwhuv duh jrrg dw iroorzlqj lqvwuxfwlrqv, exw qrw dw uhdglqj brxu plqg. - grqdog nqxwk'
c4 = 'dozdbv frgh dv li wkh jxb zkr hqgv xs pdlqwdlqlqj brxu frgh zloo eh d ylrohqw svbfkrsdwk zkr nqrzv zkhuh brx olyh. - mrkq zrrgv'

key = find_key(plain_text, cipher_text)
print(f'key : {key})

print(decrypt(c1, key))
print(decrypt(c2, key))
print(decrypt(c3, key))
print(decrypt(c4, key))
'''

'''
key : 3
first, solve the problem. then, write the code. - john johnson
without requirements or design, programming is the art of adding bugs to an empty text file. - louis srygley
computers are good at following instructions, but not at reading your mind. - donald knuth
always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. - john woods
'''

# Code
def find_key(plaintext, ciphertext):
    """Return key value"""
    key_candidates = []
    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()
    #print(plaintext, ciphertext)
    if len(plaintext) == len(ciphertext): # checking whether inputs are same text.
        for text in range(len(plaintext)):
            if ciphertext[text].isalpha(): # checking whether str's elem is alphabet.
                plainorder = ord(plaintext[text]) #text to ascii decimal.
                cipherorder = ord(ciphertext[text]) #text to ascii decimal.
                # print(plainorder, cipherorder)
                key_candidate = int((cipherorder - plainorder)%26) #The number of alphabet a~z is 26.
                key_candidates.append(key_candidate)
    for key_candidate in key_candidates:
        if key_candidates[0] == key_candidate: continue
        print("I Can't find the key of this ciphertext.") #If the cipyertext is written with many keys, this code will run.
        return None
    return key_candidates[0]


def decrypt(ciphertext, key):
    """Return decrypted text"""
    decryptedtext = ""
    for text in ciphertext:
        if text.isalpha():
            if text.isupper():
                if (ord(text)%ord("A") - key) >= 0:
                    decoding = ord(text) - key
                    decryptedtext = decryptedtext + chr(decoding)
                else:
                    decoding = (ord(text)%ord("A") - key) + ord("Z") + 1
                    decryptedtext = decryptedtext + chr(decoding)
                continue
            elif text.islower():
                if (ord(text)%ord("a") - key) >= 0:
                    decoding = ord(text) - key
                    decryptedtext = decryptedtext + chr(decoding)
                else:
                    decoding = (ord(text)%ord("a") - key) + ord("z") + 1
                    decryptedtext = decryptedtext + chr(decoding)
                continue
        decryptedtext = decryptedtext + text
    return decryptedtext


if __name__ == '__main__':
    plain_text = 'hello, world'
    cipher_text = 'khoor, zruog'

    c1 = 'iluvw, vroyh wkh sureohp. wkhq, zulwh wkh frgh. - mrkq mrkqvrq'
    c2 = 'zlwkrxw uhtxluhphqwv ru ghvljq, surjudpplqj lv wkh duw ri dgglqj exjv wr dq hpswb whaw iloh. - orxlv vubjohb'
    c3 = 'frpsxwhuv duh jrrg dw iroorzlqj lqvwuxfwlrqv, exw qrw dw uhdglqj brxu plqg. - grqdog nqxwk'
    c4 = 'dozdbv frgh dv li wkh jxb zkr hqgv xs pdlqwdlqlqj brxu frgh zloo eh d ylrohqw svbfkrsdwk zkr nqrzv zkhuh brx olyh. - mrkq zrrgv'

    key = find_key(plain_text, cipher_text)

    print(f'key : {key}')
    print(decrypt(c1, key))
    print(decrypt(c2, key))
    print(decrypt(c3, key))
    print(decrypt(c4, key))
