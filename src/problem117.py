class Point:
    def __init__(self, x, y):
        self.__x = x  
        self.__y = y 
    
    def Display(self):
        print(f"Point({self.__x},{self.__y})")

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y) 
        self.__r = r 
    
    def Area(self):
        return 3.14 * self.__r ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.__r
    
    def Display(self):
        print(f"Point({self._Point__x},{self._Point__y}) radius:{self.__r} area:{self.Area():.2f} perimeter:{self.Perimeter():.2f}")
def main():
    import sys
    input_line = sys.stdin.readline().strip().split()
    x = float(input_line[0])
    y = float(input_line[1])
    r = float(input_line[2])
    
    p = Point(x, y)
    p.Display()
    del p
    
    p = Circle(x, y, r)
    p.Display()
    del p

if __name__ == "__main__":
    main()