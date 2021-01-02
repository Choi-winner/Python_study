# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
# 위와 같이 pip를 사용할 수 있다.


# 내장함수 built in functions
# 예를들어 input과 같은 것이 내장함수.
# dir : 어떤 객체를 넘겨줬을 때, 그 객체가 어떤 변수와 함수를 가지고 있는지 표시.
# 
#  
print(dir())
import random
print(dir()) # random이 추가된 것. 
# 그냥 dir() 하면 지금 import되거나 내장되어 있어서 쓸 수 있는 모듈의 list.
# dir(random) 하면 random module 내부에 있는 함수.
# dir([1,2,3]) 하면, list인 [1,2,3]이므로, list에서 쓸 수 있는 함수들의 리스트가 반환됨.


# 여러가지 외장함수
# glob : 경로 내의 폴더 / 파일 목록을 조회 (윈도우 dir)
# import glob
# print(glob.glob('*.py')) # 확장자가 py인 모든 파일을 조회!
# 
# os : 운영체제에서 제공하는 기본 기능.
# import os
# print(os.getcwd()) # <- 현재 디렉토리가 어디인지 반환하는 것 getcwd
# folder = 'sample_dir' # 찾고싶은 폴더명, 없으면 만들고 싶은 폴더명.
# if os.path.exists(folder): # 만약 찾고싶은 이름을 가진 폴더가 존재하면
#     print('이미 존재하는 폴더')
#     os.rmdir(folder) # 폴더를 삭제하는 것.
#     print('폴더를 삭제했습니다.')
# else:
#     os.makedirs(folder) # 입력 folder은 만들고 싶은 디렉토리 이름.
#     print('이름이 '+folder+'인 폴더를 생성했습니다.')

# import os
# print(os.listdir()) # 현재 가지고 있는 폴더이름을 호출. glob와 비슷하게 쓰는것.


# import time # 시간 관련 함수들.
# print(time.localtime()) # 지금 시간을 표현
# print(time.strftime('%Y -%m-%d %H:%M:%S')) # 원하는 형식으로 표현가능

# import datetime
# print(datetime.date.today()) # 2021-01-02 와 같은 방식으로 날짜 정보 깔끔하게 출력.
# today = datetime.date.today() # 오늘 날짜를 today에 저장.
# td = datetime.timedelta(days = 100) # 100일 저장
# print('우리가 만난지 100일은 ', today + td) # today로부터 td만큼 지난 날짜 출력.
