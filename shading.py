import pygame, sys
import pygame.draw as draw
import math

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

def shade_quad(x1, y1, x2, y2, x3, y3, x4, y4):
    quad_width = x2-x1
    quad_height = y2-y1
    sectors = quad_width/10
    sector_width = quad_width/10
    sector_height = quad_height/10
    shade = 127

    update = True
    if update:
        for i in range(0, int(sectors)):
            poly_vertices = (
                [sector_width*i-1, sector_height*i-1],
                [sector_width*i, sector_height*i],
                [sector_width*i, 500-sector_height*i],
                [sector_width*i-1, 500-sector_height*i]
            )
            multiply_factor = i+1
            cur_polygon = pygame.draw.polygon(screen, [127/multiply_factor,127/multiply_factor,127/multiply_factor], poly_vertices, 15)
            shade -= i*12
    update = False

#print(shade_quad(0,0, 100,100, 100,400, 0,500))






running = True
while running:
    shade_quad(0,0, 100,100, 100,400, 0,500)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

running = False
