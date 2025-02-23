import pygame, math

pygame.init()

map = ["##########",
       "#        #",
       "#        #",
       "#        #",  
       "#        #",
       "#        #",
       "#        #",
       "#        #",
       "##       #",
       "##########"
       ]



blocksize = 40
mapwidth = len(map[0])
mapheight = len(map)
w, h = mapwidth*blocksize*2, mapheight*blocksize
border = 1
playerx = w/2/2
playery = h/2


fov = 60
angle = 0
player_angle = 0
rays = 20
ray_diff = fov / rays

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

font = pygame.font.SysFont('Arial', 20) # Set font
def displaytext(text, xpos, ypos):
    text = font.render((str(text)), True, (255, 255, 255)) # Set text to render as screen
    textRect = text.get_rect(topleft=(xpos, ypos)) # look at first line for position of getrect
    screen.blit(text, textRect)

def drawray():

    maxdepth = int(playery - 0)
    rayangle = player_angle - fov/2

    for ray in range(rays):
        depth = 0
        while depth < maxdepth:

            targetx = playerx + math.sin(math.radians(rayangle)) * depth  #soh
            targety = playery -  math.cos(math.radians(rayangle)) * depth #cah

            col = int(targetx // blocksize) # convert x to col
            row = int(targety // blocksize) # convert y to row

            if map[row][col] == " ":
                pygame.draw.line(screen, (0, 255, 0), (playerx, playery), (targetx, targety), 1) # green
            else:
                pass
                # pygame.draw.line(screen, (240, 155, 89), (playerx, playery), (targetx, targety), 1) # orange

            depth += 1
        rayangle += ray_diff








clock = pygame.time.Clock()
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #handle user input
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #working with radians, not degrees
        player_angle -= 1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_angle += 1



    screen.fill((0, 0, 0))

    # Grid
    for r in range(mapheight):
        for c in range(mapwidth):
            if map[r][c] == "#":
                pygame.draw.rect(screen, (191, 191, 191), (c*blocksize, r*blocksize, blocksize-border, blocksize-border))
            else:
                pygame.draw.rect(screen, (65, 65, 65), (c*blocksize, r*blocksize, blocksize-border, blocksize-border))
    
    # Player
    pygame.draw.circle(screen, (255, 0, 0), (playerx, playery), 4)

    #Ray
    drawray()

    #Text
    displaytext("Player Angle: " + str(player_angle), w*3/4, 50)
    displaytext("Start Angle: " + str("startangle"), w*3/4, 100)

    clock.tick(60)
    pygame.display.update()

pygame.quit()