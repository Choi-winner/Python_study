'''
class
init 은 생성자.
자동으로 생성되는 것. init 함수에 정의된 self를 제외한 변수의 갯수만큼
입력이 되어야만 오류가 안난다. 
Java 에서의 class와 같은 개념. 
class명은 그 class에 해당하는 인스턴스를 만들어 출력한다.
이때, 인스턴스는 각각 자신의 멤버변수를 가진다.
멤버 변수는 각 인스턴스에 딸려 다니는 것이다.
클래스 외부에서 특정 인스턴스에만 멤버변수를 추가하는 것이 가능하다.
그렇다고 해서 다른 모든 인스턴스들도 새로운 멤버변수 공간을 가지는 것이 아니다.
self는 해당 객체를 의미한다. self가 없으면 외부에서 입력방은 값 등을 가리키는 것.
class 내부에서 선언한 함수의 첫 입력은 self
'''

# super을 쓸 때에는 super() 를 쓰고, __init__의 매개변수에 self를 없이 쓴다.
# super은 상속하고 있는 클래스를 의미한다.
# 그러면 다중상속이라서 여러개의 부모 클래스가 있으면 super는 누구를 뜻하나?
# 먼저 상속한 클래스만 상속한다. 따라서 다중 상속 시에는 super쓰지말고, class이름 명시!



# 예외처리. Exception
# 에러를 만나는 상황에서 어떻게 할 지.
#    
# try: # 일단 이거 실행.   
#     print('나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
# except ValueError: #ValueError에 해당하는 에러가 발생했을 경우 아래의 문장을 실행하고 프로그램 종료. 
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err: # err에 발생하는 에러 문장이 담김.
#     print(err) # 발생하는 에러 문장을 그대로 출력할 수 있음.
# except Exception as err: # 그냥 Exception이라고 하거나 비워두면, else와 같이 남은 에러가 모두 해당.
#     print('알 수 없는 에러가 발생했습니다.')
#     print('발생된 에러는 ', err)

# IndexError : list index out of range <- 인덱스에 존재하지 않는 입력을 넣은 경우.



# 에러 발생시키기.   

# try:
#     print('한 자리 숫자 나누기 전용 계산기.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10: # 에러 케이스
#         raise ValueError # 내가 원하는 조건에 안맞는 경우, 이 이름의 에러를 발생시켜라.\
        
#     # raise erroe type 되면, 바로 except 문장으로 넘어간다. 따라서 아래의 print 한 줄은 출력되지 않음.
#     print('{0} / {1} = {2}'.format(num1 , num2, int(num1 / num2)))
# except ValueError:
#     print('잘못된 값을 입력했습니다. 말 좀 들으세요!')
# except:
#     print('알 수 없는 에러가 발생했습니다.')



# 사용자 정의 에러 처리.
# 위의 ValueError은 원래 있는 에러이다. 그래서 위에서 '{0} / {1} = {2}}'  <- 여기서 }가 하나 더 들어가서
# 에러가 나왔는데 그게 ValueError였다. 
# 사용자 정의 에러 처리하면 이런 걸 구분할 수 있다.
#  

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg # 클래스가 호출될 때 msg를 받아서 저장해둔다.
#     def __str__(self):
#         return self.msg  # 에러 메세지를 원할 때 self.msg에 있는 것을 반환해준다.   


# try:
#     print('한 자리 숫자 나누기 전용 계산기.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10: # 에러 케이스
#         raise BigNumberError('입력한 값은 {0}, {1}'.format(num1, num2)) # 내가 원하는 조건에 안맞는 경우, 이 이름의 에러를 발생시켜라.\
        
#     # raise erroe type 되면, 바로 except 문장으로 넘어간다. 따라서 아래의 print 한 줄은 출력되지 않음.
#     print('{0} / {1} = {2}'.format(num1 , num2, int(num1 / num2)))
# except ValueError:
#     print('잘못된 값을 입력했습니다. 말 좀 들으세요!')
# except BigNumberError as err: # 내가 정의한 에러차리. 
#     # err에는 BigNumberError에서 가지고 있는 mag가 저장된다.
#     print('에러가 발생했습니다. 너무 큰 숫자를 넣으셨군요!')
#     print(err) # 에러 문구 출력.
# finally:
#     print('Thank you!')

# finally <- 예외처리에서 항상 마지막에 출력되는 구문.
# 에러가 발생했든 안했든 마무리를 해주는 문구!



# 모듈. 
# 자동차의 타이어가 고장나면 타이어만 교체하면 된다. 
# 프로그램도 자동차처럼 다양한 부품을 만들어서 결함하는 것아 좋다.
# 이것이 모듈화이다.
# 같은 경로에 있으면 import해서 사용할 수 있다.  

# 기본적인 모듈 사용법.
# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갔을 때의 가격.
# theater_module.price_morning(4) 
# theater_module.price_sordier(5)

# 모듈명이 길 때에는 별명을 사용할 수 있다.
# import theater_module as mv # 별명을 지정해주는 것. mv라고 하면 theater_module을 대체
# mv.price(3) 
# mv.price_morning(4) 
# mv.price_sordier(5)

# 원하는 모듈을 완전히 옮겨오는 것. 
# 다른 모듈에 있는 함수들을 완전히 local처럼 쓸 수 있다.
# from theater_module import * # *은 전체를 의미.
# price(3)
# price_morning(3)
# price_sordier(5)


# 모듈 내에서 원하는 함수들만 local화 시키는 것.
# from theater_module import price, price_morning 
# price(3)
# price_morning(3)

# 원하는 함수만 로컬화시키되, 함수에도 별명을 붙일 수 있다.
# from theater_module import price_sordier as pr
# pr(5)



# 패키지.
# 여러개의 모듈을 모아 놓은 것을 패키지라고 한다.
#  
# import travel.thailand # import 시에는 주소의 끝이 package나 module만 된다. class는 안된다. 
# trip_to = travel.thailand.ThailandPakage() 
# # 패키지 travel. 모듈 thailand. 클래스 ThailandPakage
# # 즉, trip_to는 외부 class의 인스턴스!!
# trip_to.detail() 

# from ~ mport ~ 구문에서는 class만 가지고 오는 것도 가능하다!
# from travel.thailand import ThailandPackage



# __all__ 
#  
from travel import * # 이 * 표시는 __all__ 리스트에 있는 모듈명 전체를 뜻하는 것. 
trip_to = vietnam.VietnamPakage()
trip_to.detail()
# __init__모듈에서의 __all__ = ['vietnam'] <- 이라고 하면,
# all(*)로 import한 사람에서 vietam만 보여주는 것.
# 이렇게 되면 thailand는 보이지 않는다.
# 따라서, 외부에서 사용할 모듈 명을 명시적으로 __init__에 적어주어야 한다.

# __name__ == __main__ 이면 -> 직접 module을 실행하고 있는 경우.
# __name__ != __main__ 이면 -> 외부 module에서 해당 module을 import해서 쓴 경우.


import inspect
import random
print(inspect.getfile(random))
# 위 문장의 결과: C:\Program Files\Python38\lib\random.py
print(inspect.getfile(thailand))
# 위 문장의 결과: c:\Users\PC1\Desktop\PYTHONWORKSPACE\travel\thailand.py