import pygame, sys
import pygame.draw as draw
import math
#
pygame.init()

width = 500
height = 500

resolution = 50

screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

def shade_quad(x1, y1, x2, y2):
    quad_width = x2-x1
    quad_height = y2-y1
    sectors = quad_width/resolution
    sector_width = quad_width/resolution
    sector_height = quad_height/resolution
    shade = 127

    update = True
    if update:
        for i in range(0, int(resolution)):
            poly_vertices = (
                [sector_width*i-1, sector_height*i-1],
                [sector_width*i, sector_height*i],
                [sector_width*i, 500-sector_height*i],
                [sector_width*i-1, 500-sector_height*i]
            )
            multiply_factor = i+1/resolution
            cur_polygon = pygame.draw.polygon(screen, [255-multiply_factor,255-multiply_factor,255-multiply_factor], poly_vertices, 15)
            shade -= i*12
        update = False

#print(shade_quad(0,0, 100,100, 100,400, 0,500))




poly_vertices = [
    0,0,
    200,100
]

shade_quad(*poly_vertices)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
            pygame.quit()
    pygame.display.flip()
running = False
