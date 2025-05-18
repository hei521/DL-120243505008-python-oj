class Point:
    def __init__(self, x_val, y_val):
        self.__x = x_val 
        self.__y = y_val

    def displayPoint(self):
        print(f"({self.__x},{self.__y})")

if __name__ == "__main__":
    x, y = map(float, input().split())
    p1 = Point(x, y)
    p1.displayPoint()