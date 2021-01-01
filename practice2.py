# tuple <- 요소를 변경하지 않고 사용해야할 때, list말고 tuple을 사용.
# 내용 변경과 추가는 불가능하다. 하지만, 속도는  list보다 빠르다.
# 소괄호로 묶고 콤마로 구분해주면 tuple이 된다. 괄호로 묶지 않아도 된다.
menu = ('아메리카노', '카페라떼')
print(menu[0])
print(menu[1])

(starter, main, dessert) = ('스타터', '메인디쉬', '디저트')
print(starter, main, dessert)

# 요소가 1개인 tuple을 만들고 싶을 때.
single_element = 'one',  # 뒤에 콤마를 붙여서 tuple인 것을 알림.

# range 사용하여 tuple 생성.
a = tuple(range(5)) # 0부터 시작하고, 5 직전까지 범위가 tuple에 저장됨. 0,1,2,3,4
b = tuple(range(3, 7)) # 3부터 시작하고, 7 직전의 범위가 tuple에 저장됨. 3,4,5,6

# range에 증가폭을 설정하는 것도 가능하다. 증가폭은 3번째 인자.
c = tuple(range(-2, 12, 2))
print(c) # -2 부터 2씩 증가하고, 12직전인 11까지 이므로 마지막 요소는 10.

# tuple to list
# tuple 안에 list를 넣으면 lsit의 내용이 tuple이 된다.
list_1 = [1, 2, 3, 4]
tuple_1 = tuple(list_1)
print(tuple_1) # tuple이 출력 (1, 2, 3, 4)

# list to tuple
list_2 = list(tuple_1)
print(list_2) # list가 출력 [1, 2, 3, 4] 



# set. 집합.
# 중복이 불가능하고, 순서가 없는 것.
my_set = {1, 2, 3, 2, 3} # 사전과 중괄호를 쓰는 것은 같은데, 키가 없이 값만 쓰는 것이 집합.
print(my_set) # 증복이 없으니깐 1, 2, 3만 출력.

choi =  {'man', 'programmer', 'daddy'}
park = set(['woman', 'programmer', 'mommy']) # list를 set으로 변환

# 교집합
print(choi & park) # 교집합이 출력.
intersec = choi.intersection(park)
print(intersec)
print(choi)
choi.intersection_update(park)
print(choi) # 이건 choi에 교집합을 덮어쓰는 것.

# 합집합
print(choi | park)
print(choi.union(park))

# 차집합
print(park - choi)
print(park.difference(choi))

# set에 add
choi.add('daddy')
print(choi)

# set에 remove 
choi.remove('daddy') # 없는거 제거하려고 하면 key error

# 자료구조의 변경



# if
# a = input('정수를 입력하세요: ') # 프린트되는 문장 뒤에 커서가 있고, 입력을 받아 반환한다.
# if a % 3 == 0:
#     print('a 가 3의 배수입니다.')
# elif a % 3 == 1:
#     print('a 가 3N+1 입니다.')
# else:
#     print('a 가 3N+2 입니다.')

# 조건문의 조건 뒤에는 ' : ' 가 있어야합니다.



# for
for i in range(1,5): 
   print(i) 
for i in ['아이언맨', '헐크', '토르']:
    print('{0} 고객님 커피 준비되었습니다.'.format(i))


# while
i = 0
while i <= 3:
    print('현재 값은 {0}입니다.'.format(i))
    i += 1



# continue & break
# continue는 아래의 문장을 실행시키지 않고 다음 반복으로 계속하라는 것.
# break는 다음의 반복을 실행시키지 않고 반복문 탈출.
student = list(range(1,11))
tom = 7
for call in  student:
    if call == tom:
        print('{0} is tom.'.format(call))
        break
    print('{0} is not tom'.format(call))



# 한줄로 끝내는 for문
students = [1,2,3,4,5]
students = [100+i for i in students]
print(students)

students2 = ['aaa', 'bbbb', 'ccccccc']
students2_length = [len(i) for i in students2]
print(students2_length)

students2_upper = [i.upper() for i in students2]
print(students2_upper)









