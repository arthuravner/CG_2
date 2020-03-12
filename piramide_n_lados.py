from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

vertices = []
linhas = []
faces = []
facesBase = []
 
n = 20 #número de lados
r = 2 #raio
a = 2*math.pi/n #ângulo

vertices += [[0,1,0]]

for i in range(0,n):
    x = r*math.cos(i*a)
    y = 0
    z = r*math.sin(i*a)
   
    vertices += [[x,y,z]]
    linhas += [[0, i+1]]

    if(i < n-1):
        faces += [[0, i+1, i+2]]
    else:
        faces += [[0, i+1, 1]]  

    if(i < n-1):
        facesBase += [[n+1, i+1, i+2]]
    else:
        facesBase += [[n+1, i+1, 1]]                          

vertices += [[0,0,0]] # vértice n + 1

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )   

def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cores[i%len(cores)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

    #desenha base
    glBegin(GL_TRIANGLES)
    i = 0
    for face in facesBase:
        glColor3fv(cores[i%len(cores)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(180,45,45,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
