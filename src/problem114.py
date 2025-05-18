class Point:
    def __init__(self, xx, yy):
        self.__x = xx  
        self.__y = yy  
    
    def Display(self):
        print(f"Point({self.__x},{self.__y})", end=' ')

class Circle(Point):
    def __init__(self, xx, yy, rr):
        super().__init__(xx, yy)  
        self.__r = rr 
    
    def Area(self):
        return 3.14 * self.__r ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.__r
    
    def Display(self):
        super().Display()  
        print(f"radius:{self.__r} area:{self.Area():.2f} perimeter:{self.Perimeter():.2f}")


def main():
    import sys
    input_line = sys.stdin.readline().strip()
    x, y, r = map(float, input_line.split())
    C = Circle(x, y, r)
    C.Display()

if __name__ == "__main__":
    main()