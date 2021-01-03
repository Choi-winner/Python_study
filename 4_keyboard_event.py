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


# splite (=캐릭터) 불러오기
character = pygame.image.load('C:/Users/PC1/Desktop/PYTHONWORKSPACE/pygame_basic/character.png')
character_size = character.get_rect().size # 사각형 크기를 반환.
character_width = character_size[0] # 캐릭터의 가로 크기.
character_height = character_size[1] # 캐릭터의 세로 크기.
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 가운데에 해당하는 곳에 위치하도록.
character_y_pos = screen_height - character_height  # 화면 세로의 가장 아래에 해당하는 곳에 위치.


# 이동할 좌표
to_x = 0
to_y = 0



# 이벤트 루프가 실행되고 있어야 게임 창이 꺼지지 않는다.
running = True 
while running:
    for event in pygame.event.get(): # 이벤트가 발생하였는가?
        # 사용자의 입력이 있는지 확인하고, 이벤트가 발생하면 for문 실행 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인.
            if event.key == pygame.K_LEFT: # 왼쪽 키가 눌려졌다면
                to_x -= 1 # 이동하는 크기가 x축으로 -5
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP: # 방향키가 떼면 멈추어야함. <- 방향키를 뗀 것도 입력이구나
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 # 왼쪽이나 오른쪽 방향키를 떼면 to_x에 0을 넣어준다.
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0 # 위쪽이나 아랫쪽 방향키를 떼면 to_y에 0을 넣어준다.

    
    character_x_pos += to_x # 매 while loop마다 현재 캐릭터의 위치를 업데이트
    character_y_pos += to_y

    if character_x_pos < 0: # 화면 왼쪽으로 벗어나려고 하는 상황.
        character_x_pos = 0 # 화면 맨 왼쪽 이상으로 못가게 막음.
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)
    if character_y_pos < 0 : # 화면 위로 벗어나려고 하는 상황.
        character_y_pos = 0 # 화면 맨 위 이상으로 못가게 막음.
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = (screen_height - character_height)



    # screen.fill((0, 0, 255)) # RGB값으로 화면을 채우는 것.
    screen.blit(background, (0, 0)) # 0,0에서부터 background라는 이미지를 그려준다. 배경그리기.
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 사진을 캐릭터의 위치에서 시작해서 표현.


    pygame.display.update() # 게임 화면을 다시 그리기! 계속해서 화면을 새롭게 출력해줘야한다.



# pygame 종료
pygame.quit()


