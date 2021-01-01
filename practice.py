station = '사당'
print(station+' 행 열차가 들어오고 있습니다.')
station = '신도림'
print(station+' 행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station+' 행 열차가 들어오고 있습니다.')

print(2**3) # 2^3 = 8
print(5//3) # 5를 3으로 나누었을 때의 몫 = 1
print(5%3) # 5를 3으로 나누었을 때의 나머지 = 2

# not and or
print(not (2 > 4)) # not false 이므로 true

print((1 == 1) and ( 2 < 4)) # and로 그대로 쓴다.
print((1==1) & (2 < 4) ) # and를 &로 쓰기도 한다.

print((1 < 3) or (1 == 2)) # or
print(True | (1 == 2)) # or을 | 로 쓰기도 한다.
# True 나 False를 사용할 때에는 대문자로 시작해야 한다.


print(1 < 3 < 5) # True
print(1 < 4 > 6) # False

# abs 절댓값을 반환
print(abs(-2)) # 2
# pow 는 제곱을 해서 반환
print(pow(2, 5)) # 2^5 = 32를 반환
# max 는 입력받은 인자들 중의 최댓값을 반환
print(max(1,2,3)) # 3을 반환
# min 은 최솟값을 반환
print(min(1,2,3)) # 1을 반환
# round 는 반올림한 값을 반환 (사사오입)
print(round(1.11)) # 1
print(round(4.56)) # 5

# math library를 사용. -> from math import *
from math import *
print(floor(4.99)) # 내림이라서 4
print(ceil(3.14)) # 올림이라서 4
print(sqrt(16)) # 제곱근 16은 4

# random 함수
from random import *
print(random()) # 0.0 ~ 1.0 random number return
print(int(random() * 10)) # 0 ~ 10 미만 까지의 정수 출력
print(int(random() * 10) + 1) # 0 ~ 10 이하 까지의 정수 출력

print(randrange(1, 46)) # 1부터 46 미만의 임의의 값 생성. 
print(randint(1, 45)) # 1부터 45 이하의 임의의 정수 생성. <- 45포함!


# string을 표현하는 여러가지 방법.
sentence = '문자열이다.'
print(sentence)
sentence2 = "이것도 문자열이다."
print(sentence2)
sentence3 = """이것도 
문자열
이란 말이다.
아아~""" # 이렇게 적으면 있는 편집창에서 보이는 그대로가 저장.
print(sentence3)
sentence4 = '''이것도
문자열
인데
요오오'''
print(sentence4)


# 슬라이싱.
jumin = '960712-1234567'
print('성별: '+jumin[7])
print('연: '+jumin[0:2]) # 0 부터 2 직전까지, 즉 (0, 1)
print('월일: '+jumin[2:6]) # 2 부터 5까지.
print('생년월일: '+jumin[:6]) # 처음부터 6 직전까지.
print('뒷자리: '+ jumin[7:]) # 7부터 끝까지.
print('뒤자리(뒤에서부터): '+jumin[-7:])
# 맨 뒤 자리는 -1의 자리라고 생각한다. 즉, -7의 자리는 뒷자리 시작 자리이다.
# 그러면 -7: 이라는 것은 -7자리에서 시작하여 끝까지를 뜻한다.


#문자열 처리함수
# string.lower() <- string을 모두 소문자로
# string.upper() <- string을 모두 대문자로.
# char.isupper() <- char가 대문자인지 확인하여 True/False 를 반환
# len(string) <- string의 길이를 int로 반환하는 함수.
# string.replace("Python","Java") <- 1번 입력을 찾아서 2번 입력으로 바꾸는 함수.
# string.index("n") <- string에서 처음으로 나오는 "n"의 위치를 int로 반환
# string.index("n", 4) <- 인덱스 4 이후로 부터 나오는 "n"의 위치를 반환.
# string.find("n") <- 입력한 문자열이 있는 위치를 반환한다.
# find와 index 모두 찾는 것이 있을 때의 결과가 같다.
# find와 index의 차이는, find는 찾는 문자열이 없으면 -1을 반환하지만, index는 원하는 문자열이 없으면 에러가 난다.
# string.count("n") <- string이라는 문자열에서 해당되는 문자열이 몇 번 나오는 지 세는 것.
sentence = "Python is not Java"
print(sentence.index("is")) # 문자열이 시작되는 위치인 7이 반환됨.
print(sentence.find("n")) # 처음 등장하는 문자열의 위치가 출력됨.
print(sentence.index("n", 6)) # 인덱스 6부터 시작해서 처음 나오는 'n'의 위치를 반환
print(sentence.find("n", 6)) # index와 find는 결과가 같음.
# print(sentenc.index("n", 11)) # 이건 오류
print(sentence.find("n", 11)) # find는 오류가 나지 않고 -1을 반환.




# 문자열 포맷
# 방법1. % 을 이용하는 방법 C언어랑 비슷!
print('나는 %d 살 입니다.' % 26)
print('나는 %s 을 좋아해요.' % 'python')
print('Apple은 %c 로 시작해요.' % 'A')
print('나는 %s와 %s를 좋아해요.' %('빨간색', '파랑색'))

# 방법2. 중괄호로 포매팅하는 방법.
print('나는 {}와 {}를 좋아해요.'.format('빨간색', '파랑색'))
print('나는 {0}와 {1}를 좋아해요.'.format('빨간색', '파랑색'))
print('나는 {1}와 {0}를 좋아해요.'.format('빨간색', '파랑색')) 
# 이렇게 중괄호 안에 0부터 숫자를 집어 넣으면
# format( ) 내부의 입력이 0부터 순서대로 입력된다.

# 방법3. 
print('나는 {age}살이고, 이름은 {name}이다.'.format(age=26,name='choi'))


# 방법4.
age = 26
name = 'choi'
print(f'나는 {age}살이고, 이름은 {name}이다.') # 이렇게 f 를 적고 시작하면
# 미리 선언해둔 변수를 활용할 수 있다.



# 탈출문자 escape

# 1. 개행. \n
print('나는 \n 승현')

# 줄바꿈 없이 print함수를 끝내고 싶을 때.
print("string", end = ' ') # end = 'any end string' 이다. 즉, 끝맷고 싶은 문장 아무거나 올 수 있다.
# 그러면 마지막 문구가 출력되면서 개행은 안된다.

# 2. 
print("나는 '승현'이다.") # 이렇게 큰 따옴표 안에는 작은 따옴표 출력 가능.

# 3. 역슬래시 사용 
print('나는 \"승현\"이다.') # 역슬러시를 사용하면 가능! 위에도 역슬래시를 쓰는게 더 깔끔.

# 4. 역슬래시도 역슬래시를 앞에 써서 표시.
print('http\\df\\asgasg\\hffhsa')

# 5. \r 
print('red apple\rPine') # \r는 커서를 문장의 맨 앞으로 옮긴다.
# 따라서, Pine은 문장의 맨 앞부터 insert되어 결과는 Pineapple이 출력.

# 6. \b  <- back space(한 글자 삭제.)
print('Redd\bapple') # 이러면 \b 앞의 한 char 삭제한다. 

# 7. \t <- tap 역할을 하는 것.
print('Red/tApple') # 사이에 tap을 넣어주는 역할.



# List

train = ['유재석', '조세호', '정형돈']
print('train: ', train)

# listname.index('list content') 하면 리스트 콘텐츠의 인덱스가 출력
print('train index of \'조세호\' : ', train.index('조세호'))
# append <- 맨 뒤에 입력 
train.append('하하') # train의 맨 뒤에 '하하'를 입력.
print('train: ', train)
# 인덱스의 위치에 입력.
train.insert(1, '박명수') # 2번째 자리에 박명수를 입력.
print('train: ', train)
# pop 맨 뒤에서 부터 꺼내고 리스트에서는 삭제.
print(train.pop())
# count 같은 내용은 콘텐츠가 몇 개인지 확인하기.
train.append('유재석')
print(train.count('유재석')) # 2가 나옴.

# range로 list 선언하기.


# 정리하기. 
num_list = [2, 4, 5, 1, 3]
num_list.sort()
print(num_list) # 1,2,3,4,5 순서대로 나옴. 오름차순으로 정리.

# 순서 뒤집기.
num_list.reverse()
print(num_list) # 내림차순으로 정리됨.

# 삭제하기.
num_list.clear()
print(num_list) # 비어있는 리스트 출력,

# 리스트는 자료형의 종류에 구애받지 않고 여러개의 자료형을 하나의 리스트에
# 입력할 수 있다.
mixed_list = ['최승현', 26, 183]

# 여러개의 리스트를 하나의 리스트로 합치는 것도 가능.
num_list.extend(mixed_list) # 이러면 앞의 리스트에 추가되는 것.
print(num_list) 



# 사전 <- 사전은 순서가 없고, 키와 값으로 이루어진 것.
# 사전 자료형은 key와 value로 이루어 진다. 키와 값을 합쳐서 item이라고 부른다.

# key에 대한 중복은 절대 허용되지 않는다. value는 중복이 가능하다.
cabinet = {3:'유재석', 100:'정형돈', 23:'하하'}
print(cabinet[3]) # 유재석 출력
print(cabinet.get(3)) # 동일하게 유재석 출력

# 그냥 대괄호를 이용했을 경우에는 없는 key를 찾으면 오류가 난다.
# get을 이용했을 때에는 없는 key를 찾으면 None 이 출력된다. 오류가 안난다.
print(cabinet.get(5)) # 5에 아무것도 없으므로 None이 출력.
print(cabinet.get(5, '승현이')) # 5에 아무것도 없으면 '승현이'를 입력하고 그를 가지고 온다. 

# 특정한 key가 사전에 있는 지 없는 지를 확인하는 방법. 'in'을 활용.
print(3 in cabinet) # 이면 있으면 True, 없으면 False가 출력.

# 새로운 값을 사전에 입력하고 싶을 때.
# 이건 순서가 없으니깐 append가 필요없고, 그냥 변수 선언하듯 입력하면 된다.
cabinet[24] = 'kim'
print(cabinet[24])
print(cabinet)

# 없애고 싶으면 del 을 이용한다.
del cabinet[24] # key 24에 있는 아이템이 삭제된다.
print(cabinet)

# key들만 출력
print(cabinet.keys())
# value들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())  # (3, '유재석') 와 같이 출력된다.

# 사전을 없애는 것.
cabinet.clear()
