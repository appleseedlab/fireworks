import sys
import pygame
import random
import math
from time import sleep

class Tracer(pygame.sprite.Sprite):
    def __init__(self, shape, color, size, x, y, theta, v0, drag, traces,
                 alpha, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.shape = shape
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.theta = float(theta)
        self.v0 = v0
        self.drag = drag
        self.traces = traces
        self.alpha = alpha
        self.groups = groups

        self.t = 0

        self.image = pygame.Surface((4, 4))
        self.image.set_alpha(self.alpha)
        pygame.draw.circle(self.image, self.color(self.theta), [2, 2], 2)
        self.rect = self.image.get_rect(center=(int(x), int(y)))

    def update(self):
        rad = self.theta * math.pi / 180.
        v = self.v0 + -self.drag * self.t
        r = (self.v0 + v) * self.t / 2
        r = r * self.shape(self.theta)
        r = self.size * r
        x = self.x + r * math.cos(rad)
        y = self.y + r * math.sin(rad)
        if v > 0:
            self.t += 1
            if self.traces > 0: 
                Tracer(self.shape, self.color, self.size, self.x, self.y,
                       self.theta, self.v0, self.drag, self.traces - 1,
                       self.alpha / 1.3, self.groups)
                self.traces = 0
        else:
            self.kill()

        pygame.draw.circle(self.image, self.color(self.theta), [2, 2], 2)
        self.rect = self.image.get_rect(center=(int(x), int(y)))
            
def hsl(h, s, l):
    h = float(h)
    s = float(s) / 100
    l = float(l) / 100
    chroma = (1 - math.fabs(2*l - 1)) * s
    hprime = h / 60
    x = chroma * (1 - math.fabs(hprime % 2 - 1))
    m = l - chroma / 2
    print hprime, m
    if 0 <= hprime < 1:
        rgb = (chroma , x , 0)
    elif 1 <= hprime < 2:
        rgb = (x , chroma , 0)
    elif 2 <= hprime < 3:
        rgb = (0, chroma , x )
    elif 3 <= hprime < 4:
        rgb = (0, x , chroma )
    elif 4 <= hprime < 5:
        rgb = (x , 0, chroma )
    elif 5 <= hprime < 6:
        rgb = (chroma , 0, x )
    else:
        rgb = (0, 0, 0)
    rgb = map(lambda x : (x + m) * 255, rgb)
    return rgb

def start(shape, color):
    startMany([shape], [color])

def startMany(shapes, colors):
    # Window dimensions
    pygame.display.init()
    pygame.display.set_caption('cSplash \'12 Fireworks')

    width = 1280
    height = 800
    screen_size = width, height
    screen = pygame.display.set_mode(screen_size)

    bg = pygame.image.load('skyline.png')
    bg = pygame.transform.smoothscale(bg, screen_size).convert()
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    black = 0, 0, 0
    Sprites = pygame.sprite.RenderUpdates()
    info = pygame.display.Info()

    pygame.mixer.init()
    explosion = pygame.mixer.Sound('boom.aif')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN and pygame.K_SPACE \
                    or event.type == pygame.MOUSEBUTTONDOWN:
                shape = random.choice(shapes)
                color = random.choice(colors)
                x = int(random.uniform(100, info.current_w - 100))
                y = int(random.uniform(0 + 80, info.current_h * 1 / 2 - 80))
                size = random.uniform(.5, .8)
                explosion.play()
                for i in range(0, 360, 12):
                    Tracer(shape, color, size, x, y, i, 15, .62, 10, 200,
                           Sprites)

        Sprites.clear(screen, bg)
        Sprites.update()
        dirty = Sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
