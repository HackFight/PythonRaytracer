from render_math import *
class Camera:
    def __init__(self, position=vec3(), up=vec3(0,0,1), right=vec3(1,0,0), aspectRatio=16.0/9.0, focalLength=1):
        self.position = position
        self.up = up
        self.right = right
        self.aspectRatio = aspectRatio
        self.focalLength = focalLength