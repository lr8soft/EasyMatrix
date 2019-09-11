from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import EasyMatrix as em
import time
import math
testVertexShader = """
#version 330 core
in vec4 display_coord;
uniform mat4 mvp_mat;
void main(){
    gl_Position=mvp_mat*display_coord;
}
"""
testFragShader = """
#version 330 core
out vec4 draw_frag;
void main(){
    draw_frag=vec4(0.1,0.5,0.6,1.0);
}
"""
def infoInit():
    testVertex = np.array(
        [[0.5, 0.0, 0.0], [-0.5, 0.0, 0.0], [0.0, 0.5, 0.0]],dtype="float32")
    global vao
    global vbo
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER,vbo)
    glBufferData(GL_ARRAY_BUFFER,testVertex.nbytes,testVertex,GL_STATIC_DRAW)
    glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,0,None)
    glEnableVertexAttribArray(0)

def shaderInit():
    global program_handle
    program_handle = glCreateProgram()
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    frag_shader = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vertex_shader,testVertexShader)
    glShaderSource(frag_shader,testFragShader)
    glCompileShader(vertex_shader)
    glCompileShader(frag_shader)

    glAttachShader(program_handle,vertex_shader)
    glAttachShader(program_handle, frag_shader)

    glLinkProgram(program_handle)
    glUseProgram(program_handle)
def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    global vao
    global program_handle
    mvp_mat = em.rotate(time.perf_counter(),time.perf_counter(),3*time.perf_counter())
    mvp_mat *= em.scale(0.5,0.5,0.5)
    mvp_mat *= em.translate(math.sin(time.perf_counter()),math.cos(time.perf_counter()))
    location = glGetUniformLocation(program_handle,"mvp_mat")
    glUniformMatrix4fv(location,1,GL_FALSE,mvp_mat)

    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES,0,3)
    glutSwapBuffers()
if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640,480)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA)
    glutCreateWindow("Py OGL Test")
    glutDisplayFunc(render)
    glutIdleFunc(render)
    shaderInit()
    infoInit()
    glutMainLoop()