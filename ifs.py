import pygame
from random import *
from math import *
from numpy import ones

SIZE = 1000

class IFS:
    def __init__ (self, iters = 1000000):
        self.func = []
        self.color = (0, 0, 0)
        self.background = (255, 255, 255)
        self.iters = iters
        self.vis = ones ((SIZE, SIZE))

    def add_function (self, coefficients, prob):
        self.func.append ((coefficients [0], coefficients [1], prob))

    def coo (self, a, delta, mag):
        return int (SIZE - delta - mag * a)

    def get_color (self, n):
        r = self.color [0]/log (n+1)
        g = self.color [1]/log (n+1)
        b = self.color [2]/log (n+1)
        ret = (ceil (r), ceil (g), ceil (b))
        return ret

    def draw (self, dx = 500, dy = 500, mag = 50):
        scr = pygame.display.set_mode ([SIZE, SIZE])
        scr.fill (self.background)
        pxlarray = pygame.PixelArray (scr)
        x = 0
        y = 0
        for i in range (self.iters):
            choice = uniform (0.0, 1.0)
            act = 0
            for f in self.func:
                act += f [2]
                if choice <= act:
                    xt = f [0] [0] * x + f [0] [1] * y + f [0] [2]
                    yt = f [1] [0] * x + f [1] [1] * y + f [1] [2]
                    break;
            x = xt
            y = yt
            X, Y = self.coo (x, dx, mag), self.coo (y, dy, mag)
            if X >= SIZE or Y >= SIZE or X < 0 or Y < 0:
                continue
            self.vis [X] [Y] += 1
            pxlarray [X, Y] = self.get_color (self.vis [X, Y])
        pygame.display.flip ()
        while True:
            key = pygame.event.poll ()
            if key.type == pygame.KEYDOWN and key.key == pygame.K_ESCAPE:
                pygame.quit ()
                break
            pygame.time.delay (50)

