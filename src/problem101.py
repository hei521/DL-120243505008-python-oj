import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def isTriangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False
    
    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


if __name__ == "__main__":

    sides = list(map(float, input().split()))
    a1, b1, c1 = sides[0], sides[1], sides[2]
    a2, b2, c2 = sides[3], sides[4], sides[5]
    
 
    t1 = Triangle(a1, b1, c1)
    t2 = Triangle(a2, b2, c2)
    

    if t1.isTriangle() and t2.isTriangle():
      
        total_area = t1.getArea() + t2.getArea()
        
        if total_area.is_integer():
            print(int(total_area))
        else:
            print("{0:.4f}".format(total_area))
    else:
        print("failure")