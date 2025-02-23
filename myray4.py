import pygame

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
w, h = mapwidth*blocksize, mapheight*blocksize
border = 1
playerx = w/2
playery = h/2
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

def drawray():
    maxdepth = int(playery - 0)

    for ray in range(-5, 5):
        depth = 0
        while depth < maxdepth:

            targetx, targety = pygame.mouse.get_pos()

            targetx = targetx - int(10/2) * (ray*2)

            col = int(targetx // blocksize)
            row = int(targety // blocksize)

            if map[row][col] == " ":
                pygame.draw.line(screen, (0, 255, 0), (playerx, playery), (targetx, targety), 1)
            else:
                pygame.draw.line(screen, (240, 155, 89), (playerx, playery), (targetx, targety), 1)

            depth += 1

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


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

    clock.tick(60)
    pygame.display.update()

pygame.quit()