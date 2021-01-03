import pygame
#####################################################
#기본초기화 (반드시 해야하는 것)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기를 설정.
screen_width = 480 # 가로 크기.
screen_height = 640 # 세로 크기.
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정.
pygame.display.set_caption('CHOI Game') # 게임 이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)


running = True 
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정.

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트가 발생하였는가?
        # 사용자의 입력이 있는지 확인하고, 이벤트가 발생하면 for문 실행 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.
        
    # 3. 게임 캐릭터 위치 처리.
   
    # 4. 충돌 처리

    # 5. 화면에 그리기
   
    pygame.display.update() # 게임 화면을 다시 그리기! 계속해서 화면을 새롭게 출력해줘야한다.

# pygame 종료
pygame.quit()