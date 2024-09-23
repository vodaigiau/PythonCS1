import pygame
import sys

#Khởi tạo game
pygame.init()

#Tạo cửa sổ window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game galaxy")

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
ninja_image = pygame.image.load("./men.png")
#giữ đúng tỷ lệ hình gốc , vừa muốn ảnh nhỏ lại
#8334x8334 => 8334/40 => ~200
# 600X600 => 600/3 => 200
ninja_image = pygame.transform.scale(ninja_image,(ninja_image.get_width()/3, ninja_image.get_height()/3))
x_ninja = 0
y_ninja = 0

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
    time_title = font_game.render(f'Time: {time}',True, "Pink")
    
    screen.blit(bg_image,(x_bg,y_bg) )
    
    screen.blit(score, (x_score,y_score) )
    screen.blit(ninja_image,(x_ninja,y_ninja) )
    screen.blit(time_title,(x_time,y_time) )
   
    
    #xử lý thoát vòng lặp để tắt game
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    
    # load lại màn hình
    pygame.display.flip()
    clock.tick(60) #60 khung hình 
    
    
pygame.quit()
sys.exit()