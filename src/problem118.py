import math

class Shape:
    def Area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def Perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, rr):
        self.r = rr
    
    def Radius(self):
        return self.r
    
    def Area(self):
        return 3.14 * self.r ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.r

class In_Square(Circle):
    def __init__(self, rr):
        super().__init__(rr)
    
    def Area(self):
        side = self.r * math.sqrt(2)
        return side ** 2
    
    def Perimeter(self):
        side = self.r * math.sqrt(2)
        return 4 * side

class Ex_Square(Circle):
    def __init__(self, r):
        super().__init__(r)
    
    def Area(self):
        side = 2 * self.r
        return side ** 2
    
    def Perimeter(self):
        side = 2 * self.r
        return 4 * side

def main():
    r = float(input().strip())
    
    ptr = Circle(r)
    print(f"Circle's area:{ptr.Area():.2f}")
    print(f"Circle's perimeter:{ptr.Perimeter():.2f}")
    
    ptr = In_Square(r)
    print(f"In_Square's area:{ptr.Area():.2f}")
    print(f"In_Square's perimeter:{ptr.Perimeter():.2f}")
    
    ptr = Ex_Square(r)
    print(f"Ex_Square's area:{ptr.Area():.2f}")
    print(f"Ex_Square's perimeter:{ptr.Perimeter():.2f}")

if __name__ == "__main__":
    main()