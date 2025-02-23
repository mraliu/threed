import pygame
pygame.init()

class Ray:
    def __init__(self, x, y, color, speed, angle):
        self.x = x
        self.y = y
        self.x2 = self.x
        self.y2 = self.y
        self.color = color
        self.speed = speed
        self.angle = angle
        self.block = False
    def expand(self):
        if self.angle == 90 and self.x2 < 750 and self.block == False:
            self.x2 += self.speed
    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x2, self.y2), 1)

class Object:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.x2 = self.x+length
        self.y2 = self.y+length
        self.length = length
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.length, self.length))  

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)

running = True

rays = []
objs = []

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
fps = 240
size = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            rays.append(Ray(event.pos[0], event.pos[1], GREEN, 1, 90))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            objs.append(Object(event.pos[0], event.pos[1], 50, BLUE))
    screen.fill((0, 0, 0))

    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    [obj.draw() for obj in objs]

    for ray in rays:

        for obj in objs:
            if (ray.y < obj.y or ray.y > obj.y2) or ray.x2 < obj.x:
                ray.expand()
            else:
                ray.block = True
                
        ray.draw()

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()