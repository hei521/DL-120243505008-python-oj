import math

class Shape:
    def Area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def Perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, rr):
        self.r = rr
    
    def Area(self):
        return 3.14 * self.r ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.r

class In_Triangle(Circle):
    def __init__(self, rr):
        super().__init__(rr)
    
    def Area(self):
        side = self.r * math.sqrt(3)
        return (math.sqrt(3) / 4) * side ** 2
    
    def Perimeter(self):
        side = self.r * math.sqrt(3)
        return 3 * side

class Ex_Triangle(Circle):
    def __init__(self, r):
        super().__init__(r)
    
    def Area(self):
        side = 2 * self.r * math.sqrt(3)
        return (math.sqrt(3) / 4) * side ** 2
    
    def Perimeter(self):
        side = 2 * self.r * math.sqrt(3)
        return 3 * side


def main():
    r = float(input("«Î ‰»Î‘≤µƒ∞Îæ∂: "))
    
    shapes = [Circle(r), In_Triangle(r), Ex_Triangle(r)]
    names = ["Circle", "In_Triangle", "Ex_Triangle"]
    
    for shape, name in zip(shapes, names):
        print(f"{name}:")
        print(f"Area: {shape.Area():.2f}")
        print(f"Perimeter: {shape.Perimeter():.2f}")
        print()

if __name__ == "__main__":
    main()