class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
    
    def LeftMove(self, delta_x):
        self.__x -= delta_x
    
    def UpMove(self, delta_y):
        self.__y += delta_y
    
    def displayPoint(self):
        print(f"({self.__x},{self.__y})")

if __name__ == "__main__":
    x1, y1 = map(float, input().split())
    dx = float(input())
    dy = float(input())
    x2, y2 = map(float, input().split())
    p1 = Point()
    p1.displayPoint()
    p1.setPoint(x1, y1)
    p1.displayPoint()
    p1.LeftMove(dx)
    p1.displayPoint()
    p1.UpMove(dy)
    p1.displayPoint()
    p2 = Point(x2, y2)
    p2.displayPoint()