import pygame, sys
import pygame.draw as draw
import math
#
pygame.init()

width = 500
height = 500



screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

def shade_quad(x1, y1, x2, y2, resolution, direction, steps, grad_start):
    quad_width = x2-x1
    quad_height = y2-y1
    sectors = quad_width/resolution
    sector_width = quad_width/resolution
    sector_height = quad_height/resolution
    update = True
    if update is True:
        for i in range(0, int(resolution)):
            if direction == 'left':
                poly_verts = (
                    [sector_width*i, sector_height*i-1],
                    [sector_width*i, sector_height*i],
                    [sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i]
                )
            elif direction == 'right':
                poly_verts = (
                    [500-sector_width*i, sector_height*i-1],
                    [500-sector_width*i, sector_height*i],
                    [500-sector_width*i, 500-sector_height*i],
                    [500-sector_width*i, 500-sector_height*i]
                )
            elif direction == 'up':
                poly_verts = (
                    [500-sector_width*i, 500-sector_height*i-1],
                    [500-sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i-1]
                )
            elif direction == 'down':
                poly_verts = (
                    [sector_width*i, sector_height*i-1],
                    [sector_width*i, sector_height*i],
                    [500-sector_width*i,sector_height*i],
                    [500-sector_width*i, sector_height*i-1]
                )
            multiply_factor = i+steps/resolution
            cur_polygon = pygame.draw.polygon(screen, [grad_start-multiply_factor,grad_start-multiply_factor,grad_start-multiply_factor], poly_verts, 15)
    update = False

poly_vertices = [
    0,0,
    200,200
]

shade_quad(*poly_vertices, 25, 'left', 5, 120)
shade_quad(*poly_vertices, 25, 'right', 5, 120)
shade_quad(*poly_vertices, 25, 'down', 5, 120)
shade_quad(*poly_vertices, 25, 'up', 5, 120)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
            pygame.quit()
    pygame.display.flip()
running = False
