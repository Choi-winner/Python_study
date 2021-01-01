from random import *
count = 0
for i in list(range(1,51)):
    min = randint(5,51)
    if min <= 15:
        OorX = 'O'
        count += 1
    else:
        OorX = 'X'

    print(f'[{OorX}] {i}번째 손님 (소요시간 : {min}분)')
print(f'총 탑승 승객 : {count}')