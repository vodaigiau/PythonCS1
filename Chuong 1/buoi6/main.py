import pygame #functions game lib
import sys #functions operated system

# Start game
pygame.init()
# Create game window
screen = pygame.display.set_mode((1080, 720))
#Name of game window
pygame.display.set_caption("Anh Liems")
#Font and size
font_game = pygame.font.Font('./fonts/font_game.otf', 32)
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
#Create surface text => render("content, net chu ro hay ko, mau chu")
title_game = font_game.render("New Game", True, "#36eee0")
x_title_game = SCREEN_WIDTH // 2 - title_game.get_width() // 2 
y_title_game = SCREEN_HEIGHT // 2 - title_game.get_height() // 2

line_height = 50

title_game1 = font_game.render("Introduction", True, "#36eee0")
x_title_game1 = SCREEN_WIDTH // 2 - title_game1.get_width() // 2 
y_title_game1 = SCREEN_HEIGHT // 2 - title_game1.get_height() // 2 + line_height

title_game2 = font_game.render("Setting", True, "#36eee0")
x_title_game2 = SCREEN_WIDTH // 2 - title_game2.get_width() // 2 
y_title_game2 = SCREEN_HEIGHT // 2 + line_height + line_height - title_game2.get_height() // 2 
#Display game window
running = True
while running:
    #Display text on window(surface, Oxy)
    screen.blit(title_game, (x_title_game, y_title_game))
    screen.blit(title_game1, (x_title_game1, y_title_game1))
    screen.blit(title_game2, (x_title_game2, y_title_game2))

    #Load window many times to catch movements and envents in game
    #events: user operations
    # events = pygame.event.get() - LIST (array)
    event = pygame.event.poll() # 1 time event
    if event.type == pygame.QUIT:
        running = False # stop loop when user close window
    #Close game
    
    pygame.display.flip() # Load screen

pygame.quit()
sys.exit()