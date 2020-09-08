from collections import namedtuple
from renderer.sphere import Sphere
from renderer.material import Material
from renderer.raycaster import Raycasting
from renderer.datamodifiers import color
import threading

V3 = namedtuple('Vertex3', ['x', 'y', 'z'])

ivory = Material(diffuse=color(100, 100, 80))
rubber = Material(diffuse=color(80, 10, 0))

whitesnow = Material(diffuse=color(255, 255, 255))
darksnow = Material(diffuse=color(230, 230, 230))
darkersnow = Material(diffuse=color(210, 210, 210))
black = Material(diffuse=color(0, 0, 0))
gray = Material(diffuse=color(100, 100, 100))
carrot = Material(diffuse=color(255, 151, 29))


r = Raycasting(1000, 1000)
hat_offset_x = -1.2
hat_offset_y = -2
r.scene = [
    Sphere(V3(-5.7, 0, -14), 0.2, carrot),
    Sphere(V3(-5.4, 0.5, -14), 0.2, black),
    Sphere(V3(-5.4, -0.5, -14), 0.2, black),
    Sphere(V3(-5.9, 0.5, -14), 0.1, gray),
    Sphere(V3(-6.1, 0.3, -14), 0.1, gray),
    Sphere(V3(-6.1, -0.3, -14), 0.1, gray),
    Sphere(V3(-5.9, -0.5, -14), 0.1, gray),
    Sphere(V3(-6.2, 0, -14), 0.125, gray),
    Sphere(V3(-10.4, 0, -14), 0.2, black),
    Sphere(V3(-9.4, 0, -14), 0.2, black),
    Sphere(V3(-8.5, 0, -14), 0.2, black),
    Sphere(V3(-7.7, 0, -14), 0.2, black),
    Sphere(V3(-7, 0, -14), 0.2, black),
    Sphere(V3(-6, 0, -15), 1.1, whitesnow),
    Sphere(V3(-8, 0, -16), 1.7, darksnow),
    Sphere(V3(-11, 0, -17), 2.5, darkersnow),


]
r.render()
r.outputf('out.bmp')
