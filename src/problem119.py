import math

class Shape:
    def Area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def Perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        return 3.14 * self.radius ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        return self.length * self.width
    
    def Perimeter(self):
        return 2 * (self.length + self.width)

def main():
    import sys
    input_line = sys.stdin.readline().strip().split()
    r = float(input_line[0])
    a = float(input_line[1])
    b = float(input_line[2])
    
    s = ["Circle:\n", "Rectangle:\n"]
    ptr = [Circle(r), Rectangle(a, b)]
    
    for i in range(2):
        print(s[i], end='')
        print(f"Area:{ptr[i].Area():.2f}")
        print(f"Perimeter:{ptr[i].Perimeter():.2f}")

if __name__ == "__main__":
    main()