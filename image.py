import os
from PIL import Image

class PpmImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pointer = 0
        self.data = [f"P3\n{width} {height}\n255\n"]
    
    def AppendRaw(self, data):
        self.data.append(data)
    
    def AppendPixel(self, r, g, b):
        if self.pointer >= self.width * self.height:
            raise Exception("Cannot write pixels out of bounds")
        
        pixel = (r,g,b)
        for i in range(3):
            if pixel[i] < 0 or pixel[i] > 255:
                raise Exception("Pixel values must be between 0 and 255")

        self.AppendRaw(f"{r} {g} {b} ")

        if self.pointer % self.width == self.width - 1:
            self.AppendRaw("\n")

        self.pointer += 1
    
    def WriteFile(self, path):
        with open(path, "xt") as file:
            file.writelines(self.data)
            file.close()

def ConvertImage(pathIn, pathOut, delete = False):
    with Image.open(pathIn) as img:
        img.save(pathOut)
    if delete:
        os.remove(pathIn)

if __name__ == "__main__":
    img = PpmImage(1, 1)
    img.AppendPixel(255, 255, 255)
    img.WriteFile("hi.ppm")
    ConvertImage("hi.ppm", "hi.png", True)