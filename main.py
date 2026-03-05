import os
from image import PpmImage, ConvertImage
from renderer import Camera
from render_math import *

def RayColor(r):
    spherePos = vec3(0.0, 0.0, -3.0)
    t = HitSphere(r, spherePos, 1)
    if t > 0:
        N = (r.at(t) - spherePos).normalise()
        return vec3(N.x + 1.0, N.y + 1.0, N.z + 1.0) * 0.5

    unitDir = r.direction.normalise()
    a = (unitDir.y + 1.0) * 0.5
    return vec3(0.5, 0.7, 1.0) * a + vec3(1.0, 1.0, 1.0) * (1.0 - a)

if not os.path.exists("renders"):
    os.mkdir("renders")

IMAGE_WIDTH = 960

mainCamera = Camera()
imageHeight = int(IMAGE_WIDTH / mainCamera.aspectRatio)
if imageHeight < 1: imageHeight = 1

renderImg = PpmImage(IMAGE_WIDTH, imageHeight)

viewportHeight = 2.0
viewportWidth = viewportHeight * (IMAGE_WIDTH / imageHeight)

viewportU = vec3(viewportWidth, 0.0, 0.0)
viewportV = vec3(0.0, -viewportHeight, 0.0)

pixelDeltaU = viewportU / IMAGE_WIDTH
pixelDeltaV = viewportV / imageHeight

viewportUpperLeft = vec3(0.0, 0.0, -mainCamera.focalLength) - viewportU / 2.0 - viewportV / 2.0
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