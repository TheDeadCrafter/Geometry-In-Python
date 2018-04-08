import pygame, sys
import pygame.draw as draw
import math
#
pygame.init()

width = 500
height = 500



screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

grad_start = 170
def shade_quad(x1, y1, x2, y2, resolution, direction):
    if direction == 'left':
        quad_width = x2-x1
        quad_height = y2-y1
        sectors = quad_width/resolution
        sector_width = quad_width/resolution
        sector_height = quad_height/resolution
        shade = 127
        update = True

        if update == True:
            print("A")
            for i in range(0, int(resolution)):
                poly_verts = (
                    [sector_width*i, sector_height*i-1],
                    [sector_width*i, sector_height*i],
                    [sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i]
                )
                print("B")
                multiply_factor = i+1/resolution
                print("C")
                cur_polygon = pygame.draw.polygon(screen, [grad_start-multiply_factor,grad_start-multiply_factor,grad_start-multiply_factor], poly_verts, 15)
                print("D")
                shade -= i*12
        update = False
    if direction == 'right':
        quad_width = x2-x1
        quad_height = y2-y1
        sectors = quad_width/resolution
        sector_width = quad_width/resolution
        sector_height = quad_height/resolution
        shade = 127
        update = True

        if update == True:
            print("A")
            for i in range(0, int(resolution)):
                poly_verts = (
                    [500-sector_width*i, sector_height*i-1],
                    [500-sector_width*i, sector_height*i],
                    [500-sector_width*i, 500-sector_height*i],
                    [500-sector_width*i, 500-sector_height*i]
                )
                print("B")
                multiply_factor = i+1/resolution
                print("C")
                cur_polygon = pygame.draw.polygon(screen, [grad_start-multiply_factor,grad_start-multiply_factor,grad_start-multiply_factor], poly_verts, 15)
                print("D")
                shade -= i*12
        update = False
    if direction == 'down':
        quad_width = x2-x1
        quad_height = y2-y1
        sectors = quad_width/resolution
        sector_width = quad_width/resolution
        sector_height = quad_height/resolution
        update = True

        if update == True:
            for i in range(0, int(resolution)):
                poly_verts = (
                    [sector_width*i, sector_height*i-1],
                    [sector_width*i, sector_height*i],
                    [500-sector_width*i,sector_height*i],
                    [500-sector_width*i, sector_height*i-1]
                )
                multiply_factor = i+1/resolution
                cur_polygon = pygame.draw.polygon(screen, [grad_start-multiply_factor, grad_start-multiply_factor, grad_start-multiply_factor], poly_verts, 15)
        update = False
    if direction == 'up':
        quad_width = x2-x1
        quad_height = y2-y1
        sectors = quad_width/resolution
        sector_width = quad_width/resolution
        sector_height = quad_height/resolution
        update = True

        if update == True:
            for i in range(0, int(resolution)):
                poly_verts = (
                    [500-sector_width*i, 500-sector_height*i-1],
                    [500-sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i],
                    [sector_width*i, 500-sector_height*i-1]
                )
                multiply_factor = i+1/resolution
                cur_polygon = pygame.draw.polygon(screen, [grad_start-multiply_factor, grad_start-multiply_factor, grad_start-multiply_factor], poly_verts, 15)
        update = False


poly_vertices = [
    0,0,
    200,200
]

shade_quad(*poly_vertices, 25, 'left')
shade_quad(*poly_vertices, 25, 'right')
shade_quad(*poly_vertices, 25, 'down')
shade_quad(*poly_vertices, 25, 'up')
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
            pygame.quit()
    pygame.display.flip()
running = False
