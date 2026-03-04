from image import PpmImage, ConvertImage

width, height = 3, 2
testImg = PpmImage(width, height)
testImg.AppendPixel(255, 0, 0)
testImg.AppendPixel(0, 255, 0)
testImg.AppendPixel(0, 0, 255)
testImg.AppendPixel(255, 255, 0)
testImg.AppendPixel(255, 255, 255)
testImg.AppendPixel(0, 0, 0)
testImg.WriteFile("test.ppm")
ConvertImage("test.ppm", "test.png")


width, height = 255, 255
uvImg = PpmImage(width, height)
for x in range(width):
    for y in range(height):
        uvImg.AppendPixel((x,y,0))
uvImg.WriteFile("uv-test.ppm")
ConvertImage("uv-test.ppm", "uv-test.png")