from collections import namedtuple

V3 = namedtuple('Vertex3', ['x', 'y', 'z'])

class Light(object):
    def __init__(self, position=V3(0, 0, 0), intensity=1):
        self.position = position
        self.intensity = intensity