import pygame
import sys

#Khởi tạo game
pygame.init()

#Tạo cửa sổ window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ancient Temple")

font_game = pygame.font.Font("./fonts/font_game.otf",35)
#surface Text 
score = font_game.render("Score",True, "Pink")
x_score = 0
y_score = 0

#surface Image 
bg_image = pygame.image.load("./grand-mosque-grand-bur-dubai-masjid-dubai-ancient-3840x2160-8825.jpg")
bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
x_bg = 0
y_bg = 0

#TODO: hình nhân vật game
#png , jpg
ninja_image = pygame.image.load("./men-removebg-preview.png")
#giữ đúng tỷ lệ hình gốc , vừa muốn ảnh nhỏ lại
#8334x8334 => 8334/40 => ~200
# 600X600 => 600/3 => 200
ninja_image = pygame.transform.scale(ninja_image,(ninja_image.get_width()/2, ninja_image.get_height()/2))
#TODO: Tao khung rect de xu ly va cham cho surface
ninja_rect = ninja_image.get_rect()
ninja_rect.x = 0
ninja_rect.y = 0
ninja_speed = 30

#TODO: Surface & rect cua vu khi
weapon_image = pygame.image.load("./bullet-removebg-preview.png")
weapon_image = pygame.transform.scale(weapon_image,(weapon_image.get_width()/5, weapon_image.get_height()/5))
weapon_rect = weapon_image.get_rect()
weapon_rect.x = 0
weapon_rect.y = -100
# weapon_rect.x = ninja_rect.x + ninja_image.get_width()//2 - weapon_image.get_width()//2
# weapon_rect.y = ninja_rect.y + ninja_image.get_width()//2 - weapon_image.get_height()//2
#TODO: Surface & rect cua ke dich
enemies_image = pygame.image.load("./monster.png")
enemies_image = pygame.transform.scale(enemies_image,(enemies_image.get_width()/3, enemies_image.get_height()/3))
enemies_rect = enemies_image.get_rect()
enemies_rect.x = 400
enemies_rect.y = 400

# x_ninja = 0
# y_ninja = 0

#load nhạc nền
# sound_game = pygame.mixer.Sound('./sound/sound_1.wav')
# sound_game.play(-1)
# sound_game.set_volume(0.5)

#surface Text 
# 1000ms = 1s; 60s = 1min
 #hiện lên UI
x_time =SCREEN_WIDTH//2
y_time = 0

clock = pygame.time.Clock()


running = True
while running:
    # cần load lại nhiều lần 
    
    # time =pygame.time.get_ticks()# milisecond (mili giây) hiện tại
    time = pygame.time.get_ticks() //1000 # đổi qua giây
    time_title = font_game.render(f'Time: {time} s',True, "Pink")
    
    screen.blit(bg_image,(x_bg,y_bg) )
    
    screen.blit(score, (x_score,y_score) )
    # screen.blit(ninja_image,(x_ninja,y_ninja))
    
    #TODO: Hien thi hinh trong khung rect
    pygame.draw.rect(screen, 'Red', weapon_rect)
    screen.blit(weapon_image,(weapon_rect.x,weapon_rect.y))
    
    pygame.draw.rect(screen, 'Red', ninja_rect)
    screen.blit(ninja_image,(ninja_rect.x,ninja_rect.y))
    
    pygame.draw.rect(screen, 'Red', enemies_rect)
    screen.blit(enemies_image,(enemies_rect.x,enemies_rect.y))
    
    screen.blit(time_title,(x_time,y_time) )
   
    
    #xử lý thoát vòng lặp để tắt game
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    
    #Di chuyen nhan vat(awsd)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            ninja_rect.y -= ninja_speed
        elif event.key == pygame.K_s:
            ninja_rect.y += ninja_speed
        elif event.key == pygame.K_d:
            ninja_rect.x += ninja_speed
        else:
            ninja_rect.x -= ninja_speed
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        x,y = pygame.mouse.get_pos()
        ninja_rect.x = x - ninja_image.get_width()//2
        ninja_rect.y = y - ninja_image.get_height()//2
    #event mouse
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            #Lay toa do cua chuot
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ninja_rect.x = mouse_x - ninja_image.get_width()//2
            ninja_rect.y = mouse_y - ninja_image.get_height()//2
    # De phim
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        ninja_rect.y -= ninja_speed
    elif key[pygame.K_DOWN]:
        ninja_rect.y += ninja_speed
    elif key[pygame.K_LEFT]:
        ninja_rect.x -= ninja_speed
    elif key[pygame.K_RIGHT]:
        ninja_rect.x += ninja_speed
    elif key[pygame.K_SPACE]:
        weapon_rect.x = ninja_rect.x + ninja_image.get_width()//2 - weapon_image.get_width()//2
        weapon_rect.y = ninja_rect.y + ninja_image.get_width()//2 - weapon_image.get_height()//2
    weapon_rect.x += 3
    
    
    # load lại màn hình
    pygame.display.flip()
    clock.tick(60) #60 khung hình 
    
    
pygame.quit()
sys.exit()