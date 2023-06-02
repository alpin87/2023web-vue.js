import pygame
import random

# 소스 디렉터리
DIRIMG = "img/"
DIRSRC = "source/"
BUTTONSRC = "pressbutton/"
        
# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [450, 800]
screen = pygame.display.set_mode(size)
title = "미사일 게임"
stage_img = ['stage01.png', 'stage02.png', 'stage03.png', 'stage04.png', 'stage05.png']
startpage = 'startpage.png'
end_message_img = 'endpage'
end_message_img_size = 5

background = pygame.image.load(DIRIMG + stage_img[0]).convert_alpha()
bg_y = 0
 
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock() # FPS를 위한 변수


gun_sound = pygame.mixer.Sound(DIRSRC + "gun.mp3")
font = pygame.font.Font(DIRSRC + "PretendardVariable.ttf", 20)

black = (0,0,0)
STAGE = 1


player_size = [31.5, 54.3]
player_speed = 10

monster_size = [40, 40]
monster_speed = 10

boss_size = [200, 200]

item_size = [80, 80]
item_speed = 5

obstacle_size = [100, 100]
obstacle_speed = 5

hit_effect_size = [35, 35]

a_list = []


class Element:
    monster_img = ['monster01.png', 'monster02.png', 'monster03.png']
    laser_img = ['laser01.png']
    boss_img = ['boss01.png']
    item_img = ['boost_item.png', '무적.png']
    obstacle_img = ['obstacle01.png', 'obstacle02.png']
    

    def __init__(self, x, y):
        self.image = ""
        self.x = x
        self.y = y
        self.rect = None
        self.hp = 0
        self.item_type = ""
        
    def load(self, name=""):
        if name == "player":
            self.image = pygame.image.load(DIRIMG + "player.png")
            self.image = pygame.transform.scale(self.image, player_size)
            self.rect = self.image.get_rect()
            self.rect.width = player_size[0]
            self.rect.height = player_size[1]
            self.rect.x = self.rect.x = size[0] / 2 - player_size[0] / 2
            self.rect.y = self.rect.y = size[1] * (3 / 2) - player_size[1] / 2            
            
        elif name == "monster" :
            self.monster_type = random.randint(0, len(self.monster_img) - 1)
            self.image = pygame.image.load(DIRIMG + self.monster_img[self.monster_type])
            self.image = pygame.transform.scale(self.image, [i + 10 * self.monster_type for i in monster_size])
            self.rect = self.image.get_rect()
            self.rect.width = monster_size[0]
            self.rect.height = monster_size[1]
            
            while True:
                rp = True
                self.rect.x = random.randrange(0, size[0] - monster_size[0])
                self.rect.y = random.randrange(size[1] * -1, -monster_size[1])
                for i in a_list + rock_list:
                    if self.rect.colliderect(i):
                        rp = False
                        break
                if rp:
                    break
            
            self.hp = self.monster_type * 2 + 1
            speed = STAGE + 5
            if speed > 15:
                speed = 15
            self.dy = random.randint(5, speed)
        elif name == "boss":
            self.image = pygame.image.load(DIRIMG + self.boss_img[0])
            self.image = pygame.transform.scale(self.image, boss_size)
            self.rect = self.image.get_rect()
            self.rect.width = boss_size[0]
            self.rect.height = boss_size[1]
            self.rect.x = self.x
            self.rect.y = self.y
            self.hp = 33 * STAGE
        elif name == "laser":
            self.image = pygame.image.load(DIRIMG + self.laser_img[0])
            self.image = pygame.transform.scale(self.image, laser_size)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        elif name == "bosslaser":
            self.image = pygame.image.load(DIRIMG + self.laser_img[0])
            self.image = pygame.transform.scale(self.image, [i * 3 for i in laser_size])
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        elif name == "item":
            self.item_type = random.randint(0, len(self.item_img) - 1)
            self.image = pygame.image.load(DIRIMG + self.item_img[self.item_type])
            self.image = pygame.transform.scale(self.image, item_size)
            self.rect = self.image.get_rect()
            self.rect.width = item_size[0]
            self.rect.height = item_size[1]
            self.rect.x = random.randrange(0, size[0] - item_size[0])
            self.rect.y = -item_size[1]
        elif name == "obstacle":
            self.image = pygame.image.load(DIRIMG + random.choice(self.obstacle_img))
            self.image = pygame.transform.scale(self.image, obstacle_size)
            self.rect = self.image.get_rect()

            while True:
                rp = True
                self.rect.x = random.randrange(0, size[0] - obstacle_size[0])
                self.rect.y = -obstacle_size[1]
                for i in a_list:
                    if self.rect.colliderect(i):
                        rp = False
                        break
                if rp:
                    break
            
            self.hp = 10000
        elif name == "hit_effect":
            self.image = pygame.image.load(DIRIMG + "hit_effect.png")
            self.image = pygame.transform.scale(self.image, hit_effect_size)
            self.rect = self.image.get_rect()
            self.rect.width = hit_effect_size[0]
            self.rect.height = hit_effect_size[1]
            self.rect.x = self.x
            self.rect.y = self.y
            self.end_time = 0
        
    def draw_element(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])


    def check_screen(self):
        self.rect.x = max(min(self.rect.x, size[0] - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y, size[1] - self.rect.height), 0)
        
# 게임 종료 후 로비
def EndPage():
    font = pygame.font.Font(DIRSRC + "PretendardVariable.ttf", 56)
    font.set_bold(True)
    text = font.render("SCORE". format(round(score)), True, (255, 255, 255))  
    text_score = font.render("{}". format(round(score)), True, (255, 255, 255))  
    text_score_rect = text_score.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))

    
    imglist = 1
    current_time = pygame.time.get_ticks()
    stt = 1
    image_path = DIRIMG + BUTTONSRC + end_message_img + ('0' if len(str(imglist)) == 1 else '') + str(imglist) + '.png'
    imglist = 2
    bg_y = 0
    
    while True:
        now_time = pygame.time.get_ticks() - current_time 
        screen.fill(black)
        screen.blit(background, (0, bg_y))
        screen.blit(background, (0, bg_y - size[1]))
        
        screen.blit(text_score, text_score_rect)
        screen.blit(text, text_rect)
        
        bg_y += 1
        if bg_y >= size[1]:
            bg_y = 0
            
        if now_time >= 200:
            current_time = pygame.time.get_ticks()
            image_path = DIRIMG + BUTTONSRC + end_message_img + ('0' if len(str(imglist)) == 1 else '') + str(imglist) + '.png'
            if imglist == end_message_img_size or (imglist == 1 and stt == -1):
                stt *= -1
        
            imglist += stt
            
        image = pygame.image.load(image_path)
        image_rect = image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 300))
        screen.blit(image, image_rect)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                
        clock.tick(60)


# 게임 시작 전 로비
def StartPage():
    image = pygame.image.load(DIRIMG + BUTTONSRC + startpage)
    
    opty = 255
    optystt = 5
    current_time = pygame.time.get_ticks()
    bg_y = 0
    while True:
        now_time = pygame.time.get_ticks() - current_time 
        screen.fill(black)
        screen.blit(background, (0, bg_y))
        screen.blit(background, (0, bg_y - size[1]))
        bg_y += 1
        
        if bg_y >= size[1]:
            bg_y = 0
            
        if opty >= 255 or (opty <= 0):
                optystt *= -1

        opty += optystt
        image.set_alpha(opty)
            
        image_rect = image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(image, image_rect)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        clock.tick(60)
    

playing = 0
count = 0
item_count = 0 # 아이템 사용 시간
# 아이템 효과
power = 15 # 총알 속도
shield = False

player = Element(0, 0)
player.load("player")

score = 0
loss = 0
# 몬스터 설정 

a_size = [60, 60] # 몬스터 크기
monster_count = 8


# 총알
m_list = [] # 총알 수 
laser_delay = 0

item_list = [] # 아이템
bm_list = [] # 보스 총알
hit_effects = []  # 피격 효과 객체를 저장할 리스트 생성
laser_size = [10 / 1.6, 60 / 1.6]

# 운석
rockimg = ['rock1.png', 'rock2.png']
rock_list = []  # 운석 리스트

# 보스 설정
boss_list = []

# 비행기 아이템 파밍
ditem_list = []

item_speed = 10

# 카운트 다운
StartPage()

while True:

    for event in pygame.event.get(): # 키보드나 마우스의 동작을 받아옴
        if event.type == pygame.QUIT: # 게임 종료
            playing = 1
            
    # 스테이지 변경
    if not count % 1000:
        if count // 1000 < len(stage_img):
            background = pygame.image.load(DIRIMG + stage_img[count // 1000]).convert_alpha()
        STAGE += 1
            
    background = pygame.transform.scale(background, size)
            
    # 키 입력 확인
    keys = pygame.key.get_pressed()

    # 비행선 위치 이동
    player.rect.x += player_speed * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    player.rect.y += player_speed * (keys[pygame.K_DOWN] - keys[pygame.K_UP])
    player.check_screen()
    
    
    # 레이저 장애물 충돌 이벤트
    m_list = [i for i in m_list if not any(i.rect.colliderect(k.rect) for k in rock_list)]
    

    # 화면에서 나간 미사일 지우기
    m_list = [i for i in m_list if i.rect.y < size[1]]

    # 레이저 이동
    for i in m_list:
        i.rect.y -= 10
    
    # 레이저 나가기
    if keys[pygame.K_SPACE]:
        if laser_delay == 0 :
            player_laser = Element(player.rect.x + player.rect.width / 2 - laser_size[0] / 2,
                                   player.rect.y)
            player_laser.load("laser")
            gun_sound.play()
            
            m_list.append(player_laser)
            laser_delay = power
    
    # 몬스터 생성
    for i in range(monster_count - len(a_list)):
        monster = Element(0, 0)
        monster.load("monster")
        a_list.append(monster)
    
    # 아이템
    if count % 500 == 0 :
        item = Element(0, 0)
        item.load("item")
        item_list.append(item)
        
    # 보스 레이저 이동
    for i in bm_list: 
        i.rect.y += 10
        

    # 보스 레이저 발사
    for boss in boss_list:
        if count % 100 == 0:
            boss_laser = Element(boss.rect.x + boss.rect.width / 2 - laser_size[0] * 3 / 2, boss.rect.y)
            boss_laser.load("bosslaser")
            bm_list.append(boss_laser)

    # 보스 레이저 화면 밖으로 나갔을 때
    bm_list = [i for i in bm_list if i.rect.y < size[1]]
        
    # 보스 이동
    for bs in boss_list :
        bs.rect.x = player.rect.x + player.rect.width / 2 - bs.rect.width / 2
        
    # 보스
    if count == 1000 : # 보스 생성시간 수정해야 됨
        boss = Element(size[0] / 2, 40)
        boss.load("boss")
        boss_list.append(boss)
    
    
    # 운석 생성하기
    if count % 200 == 0:
        rock = Element(0, 0)
        rock.load("obstacle")
        rock_list.append(rock)

    # 운석 이동하기
    rock_list = [rock for rock in rock_list if rock.rect.y + obstacle_speed < size[1]]
    for rock in rock_list:
        rock.rect.y += obstacle_speed
                
                
    # 몬스터 이동
    a_list = [monster for monster in a_list if monster.rect.y + monster_speed < size[1]]
    for monster in a_list:
        monster.rect.y += obstacle_speed
    
    # 외계인 vs 레이저 충돌
    for ls in m_list:
        for monster in a_list + boss_list + rock_list:
            if monster.rect.colliderect(ls.rect):
                monster.hp -= 1
                min_x = monster.rect.x
                max_x = monster.rect.x + monster_size[0] - hit_effect_size[0]
                min_y = monster.rect.y
                max_y = monster.rect.y + monster_size[1] - hit_effect_size[1]
                effect = Element(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
                effect.load("hit_effect")
                effect.end_time = count + 5
                hit_effects.append(effect)
                # 피격 효과를 일정 시간 후에 사라지게 하기 위한 타이머 이벤트 추가
                pygame.time.set_timer(pygame.USEREVENT + 2, 200, True)
    # 레이저가 충돌하면 레이저 삭제
    m_list = [i for i in m_list if not any(k.rect.colliderect(i.rect) for k in a_list + boss_list + rock_list)]
    
    # 이펙트 제거
    hit_effects = [i for i in hit_effects if count <= i.end_time]
    score += sum((i.monster_type + 1) * 2 * STAGE for i in a_list if i.hp <= 0)
    a_list = [monster for monster in a_list if monster.hp > 0]
    score += sum(100 for bss in boss_list if bss.hp <= 0)
    boss_list = [bss for bss in boss_list if bss.hp > 0]

    
                
    # 비행기 충돌시 게임 종료
    for i in a_list + boss_list + rock_list + bm_list:
        if i.rect.colliderect(player.rect) and shield == False :
            playing = 1
            
            
    # 아이템 이동 및 충돌 검사 및 능력 부여
    for i in item_list:
        i.rect.y += item_speed
        if i.rect.colliderect(player.rect):
            if item.item_type == 0:
                power = 5
                item_state = "1초 부스트"
            elif item.item_type == 1:
                shield = True
                item_state = "1초 무적"
            
    # 아이템을 먹으면 아이템 없어지게
    item_list = [i for i in item_list if not i.rect.colliderect(player.rect) and i.rect.y < size[1]]


    # 아이템 능력 발동     
    if power == 5 or shield:
        item_count += 1
        
    # 아이템 카운트가 100이 될 때 정상복구
    if power == 5 and item_count >= 100:
        power = 15
        item_count = 0
        item_state = "X"
        
    if shield:
        if item_count >= 300:
            shield = False
            item_count = 0
            item_state = "X"
            player.image.set_alpha(255)
        else:
            player.image.set_alpha(100)

    # 4-4. 그리기
    screen.fill(black)

    bg_y += 1
    if bg_y >= size[1]:
        bg_y = 0
        
    screen.blit(background, (0, bg_y))
    screen.blit(background, (0, bg_y - size[1]))
    player.draw_element()
    
    for i in m_list + a_list + rock_list + item_list + bm_list + boss_list + hit_effects:
        i.draw_element()

    # 텍스트 그리기  
    # font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf")
    text_score = font.render("score : {} ". format(round(score)), True, (255, 255, 0))  
    screen.blit(text_score, (10, 5))
    
    text_time = font.render("time : {}". format(round(count / 60)), True, (255, 255, 255))
    screen.blit(text_time, (size[0]-100, 5))
    for bss in boss_list:
        boss_hp = font.render("boss : {} ". format(bss.hp), True, (255, 255, 0))  
        screen.blit(boss_hp, (size[0]/4, 5))
        
    # FPS 설정
    clock.tick(60) # 1초에 60번 while문 반복
    count += 1
    score += 0.01
    laser_delay -= 1 if laser_delay != 0 else 0

    if playing:
        screen.fill((0, 0, 0))
        EndPage()
        pygame.quit()
        break

    # 업데이트
    pygame.display.flip()
    
# 게임 종료 
pygame.quit()
