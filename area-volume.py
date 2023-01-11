import math

class Ball:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return 4 * math.pi * self.radius ** 3 / 3


def main():
    rad = eval(input("Enter a radius: "))

    ball = Ball(rad)
    area = ball.surfaceArea()
    vol = ball.volume()
    print("The Area is: {0:6.1f}".format(area))
    print("The Volume is: {0:6.1f}".format(vol))

main()
