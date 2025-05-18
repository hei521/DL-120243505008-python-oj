class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
    
    def displayPoint(self):
        print(f"({self.__x},{self.__y})")

if __name__ == "__main__":
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    p1 = Point(x1, y1)
    p1.displayPoint()
    p1.setPoint(x2, y2)
    p1.displayPoint()