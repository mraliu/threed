import pygame
import sys
import math

#global constants
SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2               # 960
MAP_SIZE = 8                                   # 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE) # 60
FOV = math.pi / 3                              # 60 degrees
HALF_FOV = FOV / 2                             # 30 degrees
CASTED_RAYS = 1                              # 160
STEP_ANGLE = FOV / CASTED_RAYS                 # 0.375
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)          # 480

SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS
#global variables
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi

def draw_map():    
    #colors
    light_grey = (191, 191, 191)
    dark_grey = (65, 65, 65)
    
    #iterate over map    
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):            
            #calculate square index            
            square = i * MAP_SIZE + j
            
            #draw map            
            pygame.draw.rect(win, 
                light_grey if MAP[square] == '#' else dark_grey,                
                (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
MAP = ('########'
       '# #    #'    
       '# #  ###'    
       '#      #'   
       '##     #'   
       '#  ### #'   
       '#   #  #'  
       '########')

#game window
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ray-casting')
clock = pygame.time.Clock()

#game loop
while True:    
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:            
            pygame.quit()
            sys.exit(0)
    
    #update background    
    pygame.draw.rect(win, (0, 0, 0), (0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT))

    draw_map()

    pygame.draw.circle(win, (162, 0, 255), (int(player_x), int(player_y)), 12)

    start_angle = player_angle - HALF_FOV
    
    for ray in range(CASTED_RAYS): # 1 in 160     
        for depth in range(MAX_DEPTH):            
            #get ray target coordinates            
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y +  math.cos(start_angle) * depth
            
            #convert target x, y coordinates to map col, row
            col = int(target_x / TILE_SIZE)           
            row = int(target_y / TILE_SIZE)  
            
            #calculate map square index            
            square = row * MAP_SIZE + col                        
            
            #print(square)
            if MAP[square] == '#':                
                pygame.draw.rect(win, (195, 137, 38),  (col * TILE_SIZE, row * TILE_SIZE,  TILE_SIZE - 1, TILE_SIZE - 1))                                
                #draw casted ray                
                pygame.draw.line(win, (233, 166, 49), (player_x, player_y), (target_x, target_y))                                
                break
            
            #increment angle by step        
            start_angle += STEP_ANGLE
    
    #update display    
    pygame.display.flip()
    
    #set FPS    
    clock.tick(30)