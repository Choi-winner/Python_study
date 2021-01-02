# 강남, 아파트, 매매, 10억, 2010년 준공
# 마포, 오피스텔, 전세, 2억, 2007년 준공
# 송파, 빌라, 월세, 500/50, 2000년 준공

class House:
    # 매물 초기화.
    def __init__(self, location, house_type, deal_type, price, buid_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.buid_year = buid_year


    # 매물 정보 표시.
    def show_detail(self):
        print('{0} {1} {2} {3} {4}년즌공'.format(self.location, self.house_type, \
            self.deal_type, self.price, self.buid_year))

H1 = House('강남', '아파트', '매매', '10억', 2010)
H2 = House('마포', '오피스텔', '전세', '5억', 2007)
H3 = House('송파', '빌라', '월세', '500/50', 2000)

House_list = [] # list로 instance 여러개를 효율적으로 관리.
House_list.append(H1)
House_list.append(H2)
House_list.append(H3)

print('총 {0: >3}대의 매물이 있습니다.'.format(len(House_list))) # 3자리 수의 매물 정보까지는 깔끔하게 전달 가능.
for a in House_list:
    a.show_detail()

