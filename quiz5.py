# 표준 체중을 구하는 프로그램. 
# 남자: 키 * 키 * 22
# 여자: 키 * 키 * 21
# 별도의 함수에서 표준 체중을 계산하여 반환.
# 전달값은 키와 성별
# 표준체중은 소수점 둘째자리까지 표시
# -> round(1.222 , 2) 하면 결과가 소숫점 둘째 자리까지인 1.22
#   

def standard(height, sex):
    result = None
    if sex == 'M':
        result = pow(int(height)/100.0, 2)*22
    elif sex == 'W':
        result = pow(int(height)/100.0, 2)*21
    else:
        print('wrong input(sex)')
    return result

height = input('키를 입력하세요: ')
sex = input('성별을 입력하세요: ')
std_weight = round(standard(height, sex), 2)
if sex == 'M':
    print(f'키 {height}cm 남자의 표준 체중은 {std_weight}kg 입니다.')
elif sex == 'W':
     print(f'키 {height}cm 여자의 표준 체중은 {std_weight}kg 입니다.')
else:
    print('wrong input(sex)')

    