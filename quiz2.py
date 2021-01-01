# 사이트별로 비밀번호를 만들어 주는 프로그램.
# http:// 를 제외
# 처음 만나는 . 이후의 부분을 제외.
# 남은 글자 중 처음 3자리 + 글자 갯수 + 글자 내 'e' 개수 + '!'로 구성

# 입력은 http://naver.com

password = 'http://naver.com'
index = password.find('.')
password = password[7:index] # 7 ~ 12까지. 12는 '.'이 있는 곳.
print(password[:3]+str(len(password))+str(password.count('e'))+'!')
