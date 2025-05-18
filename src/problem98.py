class Rectangle:
    def __init__(self, width=0.0, height=0.0):
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height

if __name__ == "__main__":
    width, height = map(float, input().split())
    r1 = Rectangle()
    print(r1.getArea())
    r2 = Rectangle(width, height)
    print(r2.getArea())