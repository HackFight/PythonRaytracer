import os
from image import PpmImage, ConvertImage
from renderer import Camera
from render_math import *

def RayColor(r):
    if HitSphere(r, vec3(0.0, 3.0, 0.0), 1):
        return vec3(1.0, 0.7, 1.0)
    unitDir = r.direction.normalise()
    a = (unitDir.z + 1.0) * 0.5
    return vec3(0.5, 0.7, 1.0) * a + vec3(1.0, 1.0, 1.0) * (1.0 - a)

if not os.path.exists("renders"):
    os.mkdir("renders")

IMAGE_WIDTH = 960

mainCamera = Camera(vec3(0,0,0), vec3(0,0,1), vec3(1,0,0), 16.0/10.0)
imageHeight = int(IMAGE_WIDTH / mainCamera.aspectRatio)
if imageHeight < 1: imageHeight = 1

renderImg = PpmImage(IMAGE_WIDTH, imageHeight)

viewportHeight = 2.0
viewportWidth = viewportHeight * (IMAGE_WIDTH / imageHeight)

viewportU = vec3(viewportWidth, 0.0, 0.0)
viewportV = vec3(0.0, 0.0, -viewportHeight)

pixelDeltaU = viewportU / IMAGE_WIDTH
pixelDeltaV = viewportV / imageHeight

viewportUpperLeft = vec3(0.0, mainCamera.focalLength, 0.0) - viewportU / 2.0 - viewportV / 2.0
pixel0Pos = viewportUpperLeft + (pixelDeltaU + pixelDeltaV) / 2.0

for y in range(imageHeight):
    print("Lines remaining : ", imageHeight - y)
    for x in range(IMAGE_WIDTH):
        pixelPos = pixel0Pos + pixelDeltaU * x + pixelDeltaV * y
        rayDir = pixelPos - mainCamera.position
        r = ray(mainCamera.position, rayDir)

        color = RayColor(r)
        renderImg.AppendPixel(int(color.x*255), int(color.y*255), int(color.z*255))

renderImg.WriteFile("renders/render.ppm")
ConvertImage("renders/render.ppm", "renders/render.png", True)