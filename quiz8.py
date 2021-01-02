# 치킨집 주문 프로그램, 예외처리 연습
# 1보다 작거나 숫자가 아닌 입력이 들어올때, ValueError 처리.
# 출력: '잘못된 값을 입력하였습니다.'
# 재고는 10마리. 10마리 이상 시킬 수 없다. 
# 치킨 소진 시 사용자 정의 에러 'SoldOut' 을 발생.
# 출력: '재고가 소진되어 더 이상 주문을 받지 않습니다.'  

from typing import ValuesView

class SoldOut(Exception): # 사용자 정의 예외!
    pass

chicken = 10 # 치킨 갯수
standby = 1 # 대기번호
while standby <= 10: # 1마리씩 10명이 주문하면 끝나니깐 최대 10회 반복.
    try:
        order = int(input('어서오세요 몇 마리 튀겨드릴까요?'))
        if order < 1:
            raise ValueError
        chicken -= order
        if chicken < 0:
            chicken += order # 주문X 이므로 치킨 갯수는 변하지 않아서 다시 복귀시켜줌.
            raise ValueError
        elif chicken == 0:
            print('대기번호 {0}번 손님 {1}마리 주문되었습니다.'.format(standby, order))
            raise SoldOut 
        else: # 남은 치킨 개수가 양수 개인 경우
            print('대기번호 {0}번 손님 {1}마리 주문되었습니다.'.format(standby, order))
            standby += 1 # 주문 되었으면 대기번호 증가.
    except ValueError:
        print('잘못된 값을 입력했습니다.') 
    except SoldOut:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다.') 
        break # while문 탈출.