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

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (display[0] / display[1]), 1, 100)  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)  

   
    while True:
        print("Ingrese los valores de X1 y Y1:")
        x1 = float(input("Ingrese un valor para X1: "))
        y1 = float(input("Ingrese un valor para Y1: "))

        if x1 > 2 and y1 > 2: 
            print("Los valores de X1, Y1, X2 y Y2 mayor a 1")
        else:
            break

    while True:
        print("Ingrese los valores de X2 y Y2:")
        x2 = float(input("Ingrese un valor para X2: "))
        y2 = float(input("Ingrese un valor para Y2: "))
    
        if x2 > 2 and y2 > 2: 
            print("Los valores de X1, Y1, X2 y Y2 no pueden ser iguales o mayor a 1")
        else:
            break
    
    if(x1  == x2 and y1 == y2):
        print("Los valores de X1, Y1, X2 y Y2 no pueden ser iguales")
        return

    sumaX1 = 0 + x1
    sumaY1 = 0 + y1

    sumaX2 = x1 + x2
    sumaY2 = y1 + y2

    sumaX = x1 + x2
    sumaY = y1 + y2
    


    print("La suma de los dos vectores es: ", sumaX, sumaY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_axes()

        vector(0, 0, sumaX1, sumaY1)  
        vector(sumaX1, sumaY1, sumaX2, sumaY2)  
        vector(0, 0, sumaX, sumaY)  
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
