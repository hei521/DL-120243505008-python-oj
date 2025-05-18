class Rectangle:
    def __init__(self, width=10.0, height=10.0):
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height
    
    def expandN(self, n):
        self.__width *= n
        self.__height *= n

if __name__ == "__main__":
    width, height = map(float, input().split())
    n = int(input())
    r1 = Rectangle()
    print(r1.getArea())
    r2 = Rectangle(width, height)
    print(r2.getArea())
    r2.expandN(n)
    print(r2.getArea())