import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random as rd

r = 0
g = 0
b = 0

def rd_cor():
  global r, g, b
  r = rd.random()
  g = rd.random()
  b = rd.random()


def display():
  gl.glClearColor(1.0, 1.0, 1.0, 1.0)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.ShadeModel(gl.GL_SMOOTH)

  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(r, g, b)
  gl.glVertex2f(1, 1)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(-1, 1)
  rd_cor()
  gl.Color3f(r, g, b)
  gl.glVertex2f(1, -1)
  gl.glEnd()
  gl.glFlush()

  gl.glBegin(gl.GL_QUADS)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(2, 2)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex(2, -2)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(-2, -2)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(-2, 2)
  gl.glEnd()
  gl.glFlush()

  gl.glBegin(gl.GL_POLYGON)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(3, 3)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(3, -3)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(-3, -3)
  rd_cor()
  gl.glColor3f(r, g, b)
  gl.glVertex2f(-3, 3)
  rd //continuando...
