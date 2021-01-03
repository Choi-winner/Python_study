import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기를 설정.
screen_width = 480 # 가로 크기.
screen_height = 640 # 세로 크기.
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정.
pygame.display.set_caption('CHOI Game') # 게임 이름

# 배경 이미지 불러오기.
background = pygame.image.load('C:/Users/PC1/Desktop/PYTHONWORKSPACE/pygame_basic/background.png')
# \를 /로 고쳐준다!

# 이벤트 루프가 실행되고 있어야 게임 창이 꺼지지 않는다.
running = True 
while running:
    for event in pygame.event.get(): # 이벤트가 발생하였는가?
        # 사용자의 입력이 있는지 확인하고, 이벤트가 발생하면 for문 실행 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.
    
    # screen.fill((0, 0, 255)) # RGB값으로 화면을 채우는 것.
    screen.blit(background, (0, 0)) # 0,0에서부터 background라는 이미지를 그려준다. 배경그리기.
    
    pygame.display.update() # 게임 화면을 다시 그리기! 계속해서 화면을 새롭게 출력해줘야한다.



# pygame 종료
pygame.quit()


