import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_axes():
    glBegin(GL_LINES)
    # Eje X
    glColor3f(1, 0, 0) 
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    # Eje Y
    glColor3f(0, 1, 0) 
    glVertex2f(0, -1)
    glVertex2f(0, 1)
    glEnd()

def vector(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1, 1, 0)  # Amarillo
    glVertex2f(x1, y1)  # Origen del vector
    glVertex2f(x2, y2)  # Punto final del vector
    glEnd()


