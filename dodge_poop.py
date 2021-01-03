'''
[게임설명]
강아지가 하늘에서 내려오는 똥을 피하는 게임.
똥은 일정한 시간마다 계속해서 내려오고
강아지는 똥을 피할수록 점수를 획득한다.

[개선점]
1. 시간이 지나면서 똥이 빨리 내려와서 피하기 어려워지기.
-> poop_speed += 1 과 같은 식으로 속도를 loop마다 키워주면 될 듯.
2. 시간이 지나면서 강아지가 커져서 피하기 어려워지기.
-> 강아지가 느려지는 것도 난이도 조절이 되므로 dog_speed -= 1 등으로 어렵게.
3. 마지막에 점수가 출력되는 화면이 나오는 것.
'''


import pygame
from random import *
#####################################################
#기본초기화 (반드시 해야하는 것)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기를 설정.
screen_width = 1280 # 가로 크기.
screen_height = 800 # 세로 크기.
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정.
pygame.display.set_caption('Dog dodges poops') # 게임 이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경화면 
background = pygame.image.load('C:/Users/PC1/Desktop/PYTHONWORKSPACE/pygame_basic/Dodge_Poop_dog/field_1280_800.jpg')

# Dog
dog_image = pygame.image.load('C:/Users/PC1/Desktop/PYTHONWORKSPACE/pygame_basic/Dodge_Poop_dog/dog_60_80.png')
dog_size = dog_image.get_rect().size
dog_width = dog_size[0]
dog_height = dog_size[1]
# 강아지의 최초 위치는 가운데 아래.
dog_x_pos = screen_width / 2 - dog_width / 2
dog_y_pos = screen_height - dog_height

# Poop
poop_image = pygame.image.load('C:/Users/PC1/Desktop/PYTHONWORKSPACE/pygame_basic/Dodge_Poop_dog/poop_40_40.png')
poop_size = poop_image.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = 0
poop_y_pos = 0
poop = []

# Speed of dog and poop
dog_speed = 1
poop_speed = 5
level_up = 0.01 # poop_speed 를 계속 빠르게 해줄 것. level_up이 클수록 어려움!

# 이동할 좌표
to_x = 0
to_y = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 30 # 30초 동안 똥을 피해야 함.

# 생성될 똥의 갯수와 그 리스트(시작위치 포함)
# 똥의 갯수는 총 시간에 비례한다.
poop_start_y = -poop_height
poop_start_x = screen_width - poop_width
poop_per_sec = 10 # 1초에 2개의 똥이라고 설정함.
sec_per_poop = 1 / poop_per_sec
poop_num = total_time * poop_per_sec 
for i in range(1,poop_num):
    poop.append([randint(0,poop_start_x),poop_start_y-i*60])
# poop list안에 (똥의 시작 x좌표, 시작 y좌표) 입력


# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴.
# 이 line이 실행될 때의 시간을 받아온다.

running = True 
cnt = 0
while running:
    dt = clock.tick(70) # 게임 화면의 초당 프레임 수를 설정.

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트가 발생하였는가?
        # 사용자의 입력이 있는지 확인하고, 이벤트가 발생하면 for문 실행 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.

        # 사용자의 방향키가 눌렸을 때의 처리.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += dog_speed
            elif event.key == pygame.K_LEFT:
                to_x -= dog_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0 # 키에서 손을 떼면 정지시켜 줘야함.

    # 3. 게임 캐릭터 위치 처리.
    dog_x_pos += to_x * dt

    # 경과 시간 계산.
    elaped_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간 (초)

    for k in range(0,poop_num-1): 
        poop[k][1] += poop_speed
    poop_speed += level_up # 0.01정도면 많이 어려움

    # 시간이 0 이하이면 게임 종료
    if (total_time - elaped_time) <= 0:
        print('타임 아웃')
        running = False

    # 화면 밖으로 안나가도록 처리.
    if dog_x_pos < 0:
        dog_x_pos = 0
    elif dog_x_pos > (screen_width - dog_width):
        dog_x_pos = (screen_width - dog_width)

    character_rect = dog_image.get_rect()
    character_rect.left = dog_x_pos # 이동한 위치를 업데이트
    character_rect.top = dog_y_pos

    poop_rect = []
    for k in range(0,poop_num-1): 
        poop_rect.append(poop_image.get_rect()) 
        poop_rect[k].left = poop[k][0]
        poop_rect[k].top = poop[k][1]
        if character_rect.colliderect(poop_rect[k]): # dog와 poop이 충돌했는지를 확인
            print('충돌')
            running = False # 충돌하면서 게임이 종료.

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경화면 그리기.
    screen.blit(dog_image, (dog_x_pos, dog_y_pos)) # 강아지 그리기.
    for k in range(0,poop_num-1): # 0부터 59까지
        screen.blit(poop_image, (poop[k][0], poop[k][1])) # 똥 그리기.
    
    score = (pygame.time.get_ticks() - start_ticks) # 점수. 1초당 1000점
    scorer = game_font.render(str(score), True, (255, 100, 100))
    screen.blit(scorer, (10,10)) # 점수 출력
   
    pygame.display.update() # 게임 화면을 다시 그리기! 계속해서 화면을 새롭게 출력해줘야한다.

pygame.time.delay(500) # 0.5초 정도 끝나기 전에 대기.

print('종료')
# pygame 종료
pygame.quit()