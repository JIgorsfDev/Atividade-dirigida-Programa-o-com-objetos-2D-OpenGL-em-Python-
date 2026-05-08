#Crie uma cena com pelo menos três triângulos posicionados em diferentes quadrantes do plano cartesiano (SRU), e desenhe os eixos X e Y. Exiba um pequeno texto (usando glutBitmapCharacter ou similar) 
#com as coordenadas de cada triângulo.

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random as rd
import sys

r = 0
g = 0
b = 0

def cor():
   global r, g, b
   r = rd.random()
   g = rd.random()
   b = rd.random()

def teclado(tecla, x, y):
   if tecla == b'\x1b':
     glut.glutDestroyWindow(glut.glutGetWindow())
     sys.exit(0)

def point(x, y, texto):
   gl.glRasterPos2f(x, y)

   for l in texto:
      glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(l))

def vertex_point(x, y):
   gl.glPointSize(4)

   gl.glBegin(gl.GL_POINTS)
   gl.glColor3f(0, 0, 0)
   gl.glVertex2f(x, y)
   gl.glEnd()

def cartesian():
   gl.glColor3f(0, 0, 0)

   gl.glBegin(gl.GL_LINES)
   gl.glVertex2f(-1, 0)
   gl.glVertex2f(1, 0)
   gl.glVertex2f(0, -1)
   gl.glVertex2f(0, 1)
   gl.glEnd()

   point(-0.95, 0.03, 'X') #colocar exato em cima do eixo da ruim na formatação
   point(0.93, 0.03, 'X') 
   point(0.03, -0.95, 'Y')
   point(0.03, 0.93, 'Y')

def draw_triangles():
   cartesian()

   cor()
   gl.glBegin(gl.GL_TRIANGLES)
   gl.glColor3f(r, g, b)
   gl.glVertex2f(-0.6, 0.6)
   gl.glVertex2f(-0.8, 0.2)
   gl.glVertex2f(-0.4, 0.2)
   gl.glEnd()

   vertex_point(-0.6, 0.6)
   vertex_point(-0.8, 0.2)
   vertex_point(-0.4, 0.2)

   gl.glColor3f(0, 0, 0)
   point(-0.6, 0.65, '(-0.6, 0.6)')
   point(-0.8, 0.15, '(-0.8, 0.2)')
   point(-0.4, 0.15, '(-0.4, 0.2)')

   cor()
   gl.glBegin(gl.GL_TRIANGLES)
   gl.glColor3f(r, g, b)
   gl.glVertex2f(0.4, 0.2)
   gl.glVertex2f(0.8, 0.2)
   gl.glVertex2f(0.6, 0.6)
   gl.glEnd()

   vertex_point(0.4, 0.2)
   vertex_point(0.8, 0.2)
   vertex_point(0.6, 0.6)

   gl.glColor3f(0, 0, 0)
   point(0.4, 0.15, '(0.4, 0.2)')
   point(0.8, 0.15, '(0.8, 0.2)')
   point(0.6, 0.65, '(0.6, 0.6)')

   cor()
   gl.glBegin(gl.GL_TRIANGLES)
   gl.glColor3f(r, g, b)
   gl.glVertex2f(-0.4, -0.2)
   gl.glVertex2f(-0.8, -0.2)
   gl.glVertex2f(-0.6, -0.6)
   gl.glEnd()

   vertex_point(-0.4, -0.2)
   vertex_point(-0.8, -0.2)
   vertex_point(-0.6, -0.6)

   gl.glColor3f(0, 0, 0)
   point(-0.4, -0.15, '(-0.4, -0.2)')
   point(-0.8, -0.15, '(-0.8, -0.2)')
   point(-0.6, -0.65, '(-0.6, -0.6)')

def draw():
   gl.glClearColor(1.0, 1.0, 1.0, 1.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT)
   draw_triangles()
   gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("O Domínio do Espaço")
glut.glutReshapeWindow(500, 500)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
