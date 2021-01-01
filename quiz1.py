# 4일부터 28일 꺄지의 날짜 중에 하루의 날짜를 정하는 프로그램.
from random import *
from math import *
meeting_day = ceil(random()*25)+4
print('오프라인 스터디 모임 날짜는 매월 '+str(meeting_day)+'일로 선정되었습니다.')

meeting_day = randint(4,28) # 4일부터 28일까지 나올 수 있음!
print(meeting_day) 