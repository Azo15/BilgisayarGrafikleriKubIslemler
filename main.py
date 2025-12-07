import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
 
from cube import get_cut_cube_vertices, get_cut_cube_edges
from transformations import apply_isometric_projection, translate_point


def draw_line_3d(p1, p2):
    a = apply_isometric_projection(p1)
    b = apply_isometric_projection(p2)
    glBegin(GL_LINES)
    glVertex3f(a[0], a[1], a[2])
    glVertex3f(b[0], b[1], b[2])
    glEnd()


def draw_cube(vertices, edges, ox=0, oy=0, oz=0):
    verts = [translate_point(v, ox, oy, oz) for v in vertices] 
    for e in edges:
        draw_line_3d(verts[e[0]], verts[e[1]])


def draw_axes():
    glColor3f(1, 0, 0)
    draw_line_3d([0,0,0], [2,0,0])

    glColor3f(0, 1, 0)
    draw_line_3d([0,0,0], [0,2,0])

    glColor3f(0, 0, 1)
    draw_line_3d([0,0,0], [0,0,2])


def draw_label_arrow(center, offset):
    glColor3f(1.0, 0.5, 0.0)
    draw_line_3d(center, offset)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("BG Kısa Sınav - 2")

    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, display[0] / display[1], 0.1, 50)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5.5)

    vertices = get_cut_cube_vertices()
    edges = get_cut_cube_edges()

    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -5.5)

        # Eksenler
        draw_axes()

        glColor3f(1, 1, 1)

        # Küpler
        draw_cube(vertices, edges, 0, 0, 0)  # Cube-1
        draw_cube(vertices, edges, 1, 0, 0)  # Cube-2
        draw_cube(vertices, edges, 0, 1, 0)  # Cube-3
        draw_cube(vertices, edges, 0, 0, 1)  # Cube-4

        # Etiket okları
        draw_label_arrow([0.5, 0.5, 0.5], [1.7, 0.5, 0.5])   # Cube-2 sağ
        draw_label_arrow([0.5, 0.5, 0.5], [0.5, 1.7, 0.5])   # Cube-3 üst
        draw_label_arrow([0.5, 0.5, 0.5], [0.5, 0.5, 1.7])   # Cube-4 ileri

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
