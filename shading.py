import pygame, sys
import pygame.draw as draw
import math

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

def shade_quad(x1, y1, x2, y2, x3, y3, x4, y4):
    quad_width = math.sqrt((x2-x1**x2-x1)+(y2-y1**y2-y1)) #Distance formula to find width
    sectors = quad_width/10
    sector_width = quad_width/10
    sector_height = y1-y2

    for i in range(0, int(sectors)):
        '''
        poly_vertices = (
            [sector_width*i-1, sector_height*i-1],
            [sector_width*i, sector_height*i],
            [sector_width*i, 500-sector_height*i],
            [sector_width*i-1, 500-sector_height*i]
        )
        print(poly_vertices)
        #pygame.draw.polygon(screen, [0,0,0], poly_vertices, 5)
        '''
        multiply_factor = i+1
        print(sector_width*multiply_factor)

print(shade_quad(0,0, 100,100, 100,400, 0,500))



def draw():
    shade_quad(0,0, 100,100, 100,400, 0,500)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

        draw()
running = False
