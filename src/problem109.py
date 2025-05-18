import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x  
        self.__y = y 

    def display(self):
        print(f"Point({self.__x}, {self.__y})")

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

def calDistance(p1, p2):
    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()
    return math.sqrt(dx**2 + dy**2)

def main():
  
    x1 = float(input("Enter x coordinate for Point 1: "))
    y1 = float(input("Enter y coordinate for Point 1: "))
    p1 = Point(x1, y1)


    x2 = float(input("Enter x coordinate for Point 2: "))
    y2 = float(input("Enter y coordinate for Point 2: "))
    p2 = Point(x2, y2)


    print("Point 1:", end=" ")
    p1.display()
    print("Point 2:", end=" ")
    p2.display()


    distance = calDistance(p1, p2)
    print(f"Distance between the points: {distance:.2f}")

if __name__ == "__main__":
    main()