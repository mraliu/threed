import pygame

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))

GREEN = (0, 255, 0)

cube = [
[[0,0,0], [0,1,0], [0,2,0]], 
[[1,0,0], [1,1,0], [1,2,0]],
[[2,0,0], [2,1,0], [2,2,0]],
[[0,0,1], [0,1,1], [0,2,1]], 
[[1,0,1], [1,1,1], [1,2,1]],
[[2,0,1], [2,1,1], [2,2,1]],
[[0,0,2], [0,1,2], [0,2,2]], 
[[1,0,2], [1,1,2], [1,2,2]],
[[2,0,2], [2,1,2], [2,2,2]],
]

cubewidth = 50

pygame.display.set_caption('Simple Pygame Window')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    startx = w/2-(cubewidth*3/2)
    starty = h/2-(cubewidth*3/2)

    [0,0,0], [0,1,0], [0,2,0]

    for i in range(3):
        ft = cube[i][0]
        pygame.draw.circle(
            screen,
            GREEN,
            (startx+(ft[0][0]*50), starty+(ft[0][0]*50)),
            1
        )

    pygame.display.flip()

pygame.quit()
