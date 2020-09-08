from renderer.datamodifiers import *
from renderer.linearalgebra import *
from math import pi, tan
from collections import namedtuple
V3 = namedtuple('Vertex3', ['x', 'y', 'z'])



class Raycasting(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.zbuffer = []
        self.create_buffer(46, 90, 28)

    def scene_intersect(self, orig, direction):
        for obj in self.scene:
            if obj.ray_intersect(orig, direction):
                return obj.material
        return None

    def point(self, x, y, c=None):
        try:
            self.framebuffer[y][x] = c or self.current_color
        except:
            pass

    def create_buffer(self, r, g, b):
        self.framebuffer = [
            [color(r, g, b) for x in range(self.width)]
            for y in range(self.height)
        ]

        self.zbuffer = [
            [-float('inf') for x in range(self.width)]
            for y in range(self.height)
        ]

    def cast_ray(self, orig, direction):
        impacted_material = self.scene_intersect(orig, direction)
        if impacted_material:
            return impacted_material.diffuse
        else:
            return color(46, 90, 28)

    def outputf(self, filename):
        f = open(filename, 'bw')
        with open(filename, 'bw') as outf:
            outf.write(char('B'))
            outf.write(char('M'))
            outf.write(dword(14 + 40 + self.width * self.height * 3))
            outf.write(dword(0))
            outf.write(dword(14 + 40))
            outf.write(dword(40))
            outf.write(dword(self.width))
            outf.write(dword(self.height))
            outf.write(word(1))
            outf.write(word(24))
            outf.write(dword(0))
            outf.write(dword(self.width * self.height * 3))
            outf.write(dword(0))
            outf.write(dword(0))
            outf.write(dword(0))
            outf.write(dword(0))
            for x in range(self.width):
                for y in range(self.height):
                    outf.write(self.framebuffer[y][x])

    def render(self):
        fov = int(pi/2)
        for y in range(self.height):
            for x in range(self.width):
                i = 2 * ((x + 0.5)/self.width-1) * \
                    self.width/self.height * tan(fov/2)
                j = (1 - 2 * (y + 0.5)/self.height) * tan(fov/2)
                direction = norm(V3(i, j, -1))
                self.framebuffer[y][x] = self.cast_ray(V3(0, 0, 0), direction)
