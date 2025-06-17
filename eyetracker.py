import pygame
import math

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eye Tracking")

def draw_eye(eye_x, eye_y):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y

    distance = min(math.sqrt(distance_x**2 + distance_y**2), 30)
    angle = math.atan2(distance_y, distance_x)

    pupil_x = eye_x + (math.cos(angle) * distance)
    pupil_y = eye_y + (math.sin(angle) * distance)

    pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 50)  
    pygame.draw.circle(screen, (255, 105, 180), (pupil_x, pupil_y), 15)

def update():
    pass

def draw():
    screen.fill((255, 182, 193)) 
    draw_eye(200, 200)
    draw_eye(330, 200)
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw()

pygame.quit()
