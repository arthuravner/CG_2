from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

verticesBaseBaixo = []
verticesBaseCima = []

n = 20 #número de lados
r = 2 #raio
a = 2*math.pi/n #ângulo

for i in range(0,n):
    x = r*math.cos(i*a)
    z = r*math.sin(i*a)

    x1 = r/2*math.cos(i*a)
    z1 = r/2*math.sin(i*a)
   
    verticesBaseBaixo += [[x,0,z]]
    verticesBaseBaixo += [[x1,0,z1]]

    verticesBaseCima += [[x,1,z]]
    verticesBaseCima += [[x1,1,z1]]           
        
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )   

def Anilha():
    #Desenha a base de baixo da anilha
    glBegin(GL_TRIANGLE_STRIP)
    #glColor3f(1,1,0)
    i = 0
    for vertex in verticesBaseBaixo:
        glColor3fv(cores[i%len(cores)])        
        glVertex3fv(vertex)
        i = i + 1
    glVertex3fv(verticesBaseBaixo[0])
    glVertex3fv(verticesBaseBaixo[1])
    glEnd()

    #Desenha a base de cima da anilha
    glBegin(GL_TRIANGLE_STRIP)
    #glColor3f(1,1,0)
    i = 0
    for vertex in verticesBaseCima:
        glColor3fv(cores[i%len(cores)])        
        glVertex3fv(vertex)
        i = i + 1
    glVertex3fv(verticesBaseCima[0])
    glVertex3fv(verticesBaseCima[1])
    glEnd()

    #Desenha lados da anilha
    glBegin(GL_QUAD_STRIP)
    glColor3f(1,0,0)    
    glVertex3fv(verticesBaseBaixo[n-1])
    glVertex3fv(verticesBaseCima[n-1])
    for i in range(0,n):
        #glColor3fv(cores[i%len(cores)])        
        glVertex3fv(verticesBaseBaixo[i])
        glVertex3fv(verticesBaseCima[i])
    glEnd()      

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Anilha()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ANILHA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(180,45,45,1)
glutTimerFunc(50,timer,1)
glutMainLoop()    
