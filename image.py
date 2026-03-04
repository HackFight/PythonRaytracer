import os
from PIL import Image

class PpmImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pointer = 0
        self.data = f"P3\n{width} {height}\n255\n"
    
    def AppendRaw(self, data):
        self.data += data
    
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
        try:
            with open(path, "xt") as file:
                file.write(self.data)
                file.close()
        except FileExistsError:
            answer = input("File already exists, overwrite? [Y/n]: ")
            if answer.lower() != "n":
                os.remove(path)
                self.WriteFile(path)

def ConvertImage(pathIn, pathOut):
    with Image.open(pathIn) as img:
        img.save(pathOut)