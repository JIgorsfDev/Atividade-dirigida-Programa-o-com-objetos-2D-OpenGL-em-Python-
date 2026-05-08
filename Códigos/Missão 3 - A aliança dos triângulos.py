#Desenvolva uma função que desenhe triângulos isósceles com base e altura fornecidas pelo usuário. Em seguida, use essa função para desenhar pelo menos 5 triângulos com diferentes tamanhos e posições em tela. 
#Cada triângulo deve ter uma cor distinta.
#incompleto

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import sys
import random as rd

r = 0
g = 0
b = 0

def teclado(tecla, x, y):
  if tecla == b'\x1b':
    sys.exit()

def cor():
  global r, g, b
  r = rd.random()
  g = rd.random()
  b = rd.random()

def draw_triangles(x, y, bs, h):
    gl.glBegin(gl.GL_TRIANGLES)
    cor()
    gl.glColor3f(r, g, b)
    gl.glVertex2f(x, y)
    gl.glVertex2f(x + bs, y)
    gl.glVertex2f(x + bs/2, y + h)
    gl.glEnd()
   
  

  

bs = float(input("Digite a base do triangulo (entre -1 e 1): "))
h = float(input("Digite a altura do triangulo (entre -1 e 1): "))


def draw():
  gl.glClearColor(1.0, 1.0, 1.0, 1.0)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  
  cor()
  global bs, h
  x = -bs/2
  y = -h/2
  
  draw_triangles(x, y, bs, h)
  x += 0.1 #trocar isso, é pros triangulos mudarem de posição e tamanho 
  y += 0.1
  draw_triangles(x, y, bs, h)
  x += 0.1
  y += 0.1
  draw_triangles(x, y, bs, h)
  x += 0.1
  y += 0.1
  draw_triangles(x, y, bs, h)
  x += 0.1
  y += 0.1
  draw_triangles(x, y, bs, h)
  x += 0.1
  y += 0.1

  gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("A aliança dos triângulos")
glut.glutReshapeWindow(500, 500)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()

