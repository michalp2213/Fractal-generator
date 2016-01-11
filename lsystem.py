import pygame
from math import *

size = 1000

class L_system:
    def __init__ (self):
        self.axiom = ""
        self.seq = ""
        self.rules = {}
        self.angle = 90
        self.length = 5
        self.color = (0, 0, 0)
    def setAxiom (self, a):
        self.axiom = a
    def setColor (self, c):
        self.color = c
    def setAngle (self, a):
        self.angle = radians (a)
    def setLen (self, l):
        self.length = l
    def addRule (self, key, val):
        self.rules [key] = val
    def clearRules (self):
        self.rules.clear ()
    def eval (self, iters):
        tmp = self.axiom
        for i in range (iters):
            self.seq = ""
            for v in tmp:
                if v in self.rules:
                    self.seq += self.rules [v]
                else:
                    self.seq += v
            tmp = self.seq
    def draw (self, sx, sy):
        direction = 0
        dx = self.length * cos (direction)
        dy = self.length * sin (direction)
        stack = []
        scr = pygame.display.set_mode ([size, size])
        scr.fill ((255, 255, 255))
        for i in self.seq:
            if i == "F":
                pygame.draw.line (scr, self.color, (sx, sy), (sx + dx, sy + dy))
                sx += dx
                sy += dy
            elif i == "f":
                sx += dx
                sy += dy
            elif i == "+":
                direction += self.angle
                dx = self.length * cos (direction)
                dy = self.length * sin (direction)
            elif i == "-":
                direction -= self.angle
                dx = self.length * cos (direction)
                dy = self.length * sin (direction)
            elif i == "[":
                stack.append ((sx, sy, direction))
            elif i == "]":
                sx, sy, direction = stack.pop ()
            pygame.display.flip ()
        print "End"
        while True:
            key = pygame.event.poll ()
            if key.type == pygame.KEYDOWN and key.key == pygame.K_ESCAPE:
                pygame.quit ()
                break
            pygame.time.delay (50)


