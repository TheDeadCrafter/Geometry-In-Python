import pygame, sys
import pygame.draw as draw

pygame.init()
'''
Last Edited: April 3rd
If you're on github, you can get some practice with being an intepreter
I'm not gonna comment this code

Too
Much
Work

Have a nice day!

'''


width = 500
height = 500

screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])


far_y = 100
far_x = 100




def draw():
    screen.fill([255,255,255])
    poly_vertices = (
        [0,0],
        [far_x,far_y],
        [far_x,500-far_y],
        [0,500]
    )
    opp_poly = (
        [500,0],
        [500-far_x,far_y],
        [500-far_x,500-far_y],
        [500,500]
    )
    #draw.polygon(screen, [255,0,0], poly_vertices, width=0)
    draw.polygon(screen, [0,0,0], poly_vertices, 5)
    draw.polygon(screen, [0,0,0], opp_poly, 5)
    draw.line(screen, [0,0,0], [far_x,far_y], [500-far_x,far_y], 5)
    draw.line(screen, [0,0,0], [far_x,500-far_y], [500-far_x, 500-far_y], 5)

    pygame.display.flip()

delta = 1

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                far_y += delta
                far_x += delta
            elif event.key == pygame.K_DOWN:
                far_y -= delta
                far_x -= delta
    draw()

    pygame.display.flip()
running = False
