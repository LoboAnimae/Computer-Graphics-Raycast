from collections import namedtuple
from renderer.sphere import Sphere
from renderer.material import Material
from renderer.raycaster import Raycasting
from renderer.datamodifiers import color
from renderer.Light import *

V3 = namedtuple('Vertex3', ['x', 'y', 'z'])

ivory = Material(diffuse=color(100, 100, 80), albedo=0.7)
rubber = Material(diffuse=color(80, 10, 0), albedo=0.2)

whitesnow = Material(diffuse=color(255, 255, 255), albedo=0.9)
darksnow = Material(diffuse=color(230, 230, 230), albedo=0.8999)
darkersnow = Material(diffuse=color(210, 210, 210), albedo=0.88)
black = Material(diffuse=color(0, 0, 0), albedo=0.03)
gray = Material(diffuse=color(100, 100, 100), albedo=0.2)
carrot = Material(diffuse=color(255, 151, 29), albedo=0.12)


r = Raycasting(500, 500, bg=(255, 255, 255))
r.light = Light(
    position=V3(-20, 20, 20),
    intensity=1.5
)
r.scene = [
    Sphere(V3(0, 0, 0), 0.0000000001, whitesnow)
]
r.render()
r.outputf('out.bmp')
