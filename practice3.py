# 함수부터 
# 파이썬에서 함수는 def 를 통해 선언한다.
# 선언할 때에는 반환 변수 형은 정의에는 쓸 필요가 없다.
# def와 함께는 함수명과 입력 변수명만 적어주면 된다.
# 함수 마지막에 반환의 의미로 return 과 함께 반환하는 변수명을 적어주면 된다.
# 아주 간편
# 여러 개의 값을 반환하고 싶을 때에는 tuple 형식으로 콤마로 구분하여 반환하면 된다.
# 입력과 출력의 자료형과 갯수는 잘 맞춰서 적어주면 된다.
# 
# 기본값
# 함수의 입력에 기본값을 적어두면, 입력이 안들어 왔을 경우에 
# 안들어온 입력은 기본값으로 사용할 수 있다.
# 
#     

def profile(name, age = 24, school = 'Y'):
    print(f'{name}은 {age}살이고 {school}에 다닌다.')

profile("최승현", 26, 'K')
profile("박명수")
profile("박명수", 36)
# 함수의 인자는 입력된 순서대로 들어가기 때문에 
# 기본값을 가지는 인자는 항상 기본값이 없는 인자의 뒤에 와야한다.

# 키워드 값. 우리는 함수의 입력 매개변수의 이름을 키워드라고 한다.
# 이 키워드를 이용하면, 함수를 호출해서 매개변수에 어떤 값을 입력할 때에,
# 원하는 순서대로 입력할 수 있다.
profile(age = 256, school = 'SEOUL', name = 'KJH') 
# 위와 같이 순서가 제멋대로 입력되도 키워드만 정확하면 문제없다.

# 가변인자를 사용하는 방법.
# 원하는 입력의 개수가 변할 수 있을 때,
# 특정한 개수의 입력으로 정해지면 적게 입력할 때에는 함수 호출문이 귀찮고,
# 또, 선언된 매개변수의 개수보다 더 많은 입력을 넣고 싶을 때에는 함수 전체를 수정해야한다.
# 이럴때, 가변인자를 사용하면 편하다.
# *variable 로 선언하면, 이게 tuple로 된다. 
def animal(name, *region):
    print(f'{name}is lives in ',end = ' ')
    for reg in region:
        print(f'{reg} ', end = ' ')
    print()

animal('tiger', 'a', 'b', 'c')
animal('bird', 'a', 'b', 'c', 's', 'g')
# 위에 2번째 인자부터는 tuple로 묶여서 입력된다.



# 지역변수와 전역변수
# 지역변수는 함수 내에서만 존재하는 변수
# 전역변수는 프로그램 전쳉에서 존재하는 변수
# 
# 함수 내부에서 global 을 앞에 쓰고 함수 바깥의 전역변수 이름을 넣으면
# 바깥의 전역변수가 함수 내부에서 쓰이고, 초기화도 가능해진다.   

gun = 10
def checkpoint(soldiers):
    global gun # 지금 아래에 우변의 gun이 원래 없었는데 전역변수를 안에다가 넣어줌.
    gun = gun - soldiers
    print('함수 내 남은 총: {0}'.format(gun))
checkpoint(4)

# 전역변수는 권장되지 않는다.
# 매개변수를 사용하는 것이 안전.



# 표준 입출력
# sep
print('aaa' , 'bbbb' , 'cccc', sep=' VS ', end = '무엇이 이길까요?')
# sep는 콤마로 구분된 여러개의 입력이 사이에 어떤 문장이 자동으로 들어가는지.
# end는 마지막 문장 + 개행이 안되는 것. 
# 원래는 자동으로 end = '\n' 이 있는 것과 동일

# file = sys.stdout
# file = sys.stderr
#  
# 문자열을 정렬하는 방법! ljust rjust
scores = {'수학':100, '영어':24, '코딩':100}
for (subject, score) in scores.items():
    print(subject.ljust(3) ,':', str(score).rjust(4))


# 숫자를 001 002 003 004 ... 와 같이 입력하고 싶을 때, string.zfill(n) <- n은 결과로 만들 총 문자열의 길이.
for i in range(1, 21):
    print('대기번호: ', str(i).zfill(3)) # 주의 점은 string 형에 쓴다는 것.


# input 은 항상 문자열 형태로 입력을 받는다. string


# 다양한 형태의 입출력 
# {0: 이공간 } 왼쪽의 공간에 다양한 형태의 입력을 넣음으로써 출력을 다양하게 가능.
#  
asdf = 'asdf'
print('{0: >5}'.format(asdf)) 
# : 바로 오른쪽에 빈칸이 있는 것은 빈 공간을 space로 채우라는 뜻이고
# > 는 입력을 오른쪽에 정렬하라는 뜻이고, 5는 5칸을 사용하라는 뜻이다.
print('{0:_<7}'.format(asdf)) # 7칸을 사용하고 왼쪽 정렬하되 남는 공간은 _로 채워라.
num = 300
print('{0:B<+10}'.format(num)) # 10칸을 사용하고 남은 공간은 B로 채우되, 왼쪽 정렬에 입력의 부호를 명시적으로 붙여라.
print('{0: >+10}'.format(num))
# 이때. {0: <3} 의 : 오른쪽 빈 공간에는 하나의 char만 들어가야한다. string이 아니다.
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
# 위처럼 +를 써주는 것은 양수일떄는 +를 앞에 붙이고, 음수일 때에는 -를 앞에 붙이는 것.

# 3자리마다 콤마를 찍어주기.
print('{0:,}'.format(10000000000)) # 3자리마다 
# 3자리마다 콤마 찍고, 부호도 명시.
print('{0:+,}'.format(10000000000))
print('{0:+,}'.format(-10000000000))
# 3자리마다 콤마를 찍고, 부호를 명시하고, 자릿수도 확보하기. 빈자리도 ^로 채우기.
print('{0:^>+20,}'.format(10000000000)) # 콤마다 자릿수 뒤에 마지막으로 들어감.
# 소숫점을 출력.
print('{0:f}'.format(5/3))
# 소숫점을 특정 자릿 수까지만 출력.
print('{0:.2f}'.format(5/3)) 
# 위와 같이 하면, 소숫점 2자리까지 출력해달라는 것.



# 파일 입출력.

# 파일 생성 및 쓰기.
# score_file = open('score.txt', 'w', encoding='utf8') # 입력: 파일명, 여는목적, 인코딩방식(한글을 읽을려면 utf8)
# print('수학 : 100', file = score_file)
# print('영어 : 70', file = score_file)
# score_file.close()

# 파일 뒤에 이어쓰기(append). a 사용!
# score_file = open('score.txt', 'a', encoding='utf8') # a로 쓰면, 덮어쓰기 용도로 여는 것. append
# score_file.write('\n국어: 20')
# score_file.write('\n코딩: 100')
# score_file.close()

# 파일 읽어오기
# score_file = open('score.txt', 'r', encoding = 'utf8')
# str1 = score_file.read()
# print(str1)

# 파일의 내용 1줄씩 읽어오기.
score_file = open('score.txt', 'r', encoding = 'utf8')
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# readline 은 줄별로 읽고, 한 줄 읽으면 커서는 다음 줄로 이동하는 것.



