# 댓글에서 추첨해서 1명이 치킨, 3명이 커피.
# 20명이 댓글을 달았다. 아이데는 1 ~ 20 이라고 가정.
# 무작위로 추첨하고 중복으로 당첨은 불가능.
# ramdom 모듈의 shuffle 과 sample을 활용.

# 치킨 당첨자는 그냥 int
# 커피 당첨자는 list


from random import *
# random 안에 shuffle 과 sample이 있다.
lst = list(range(1, 21))
print(lst)
shuffle(lst) # lst에 있는 것의 순서를 섞는다.
print(lst)
winner = sample(lst, 2) # lst에 있는 2개를 랜덤하게 뽑는다.
print(winner)
# shffle 과 sample은 동시에 쓰는 것이 좋은가?

candidates = list(range(0, 21))
shuffle(candidates)
first_pick = sample(candidates, 4)
print('first pick: ',first_pick)
second_pick = sample(first_pick, 1)[0] #
print('second pick: ',second_pick)
first_pick.remove(second_pick)
print('''-- 당첨자 발표 --
치킨 당첨자 : {chicken}
커피 당첨자 : {coffee}
-- 축하합니다. -- '''.format(chicken = second_pick, coffee = first_pick))
# remove의 입력에는 list의 요소의 변수형이 들어가야한다.
# 그런데, list가 int로 형변환되지 않아서 오류가 발생했었다.
# 그래서 list의 첫 번째 요소가 int인 것에 착안하여 [0]으로 
# 한 요소만을 second_pick에 저장했다. 
# 원래 second_pick은 int로 저장되어야 한다.  
