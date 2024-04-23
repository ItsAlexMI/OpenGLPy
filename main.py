import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from utils import *


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glOrtho(-2, 2, -2, 2, -1, 1)  # Ajustar el volumen de visualización para alejar la cámara

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_axes()
        vector(0,0, -1, 1)  # Dibujar el vector en el plano bidimensional
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
