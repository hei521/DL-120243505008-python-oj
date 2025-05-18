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
    
    def getPerimeter(self):
        return self.a + self.b + self.c

if __name__ == "__main__":

    sides = list(map(float, input().split()))
    a1, b1, c1 = sides[0], sides[1], sides[2]
    a2, b2, c2 = sides[3], sides[4], sides[5]
    

    t1 = Triangle(a1, b1, c1)
    t2 = Triangle(a2, b2, c2)
    

    if t1.isTriangle() and t2.isTriangle():

        perimeter_diff = t1.getPerimeter() - t2.getPerimeter()
        print(int(perimeter_diff) if perimeter_diff.is_integer() else perimeter_diff)
    else:
        print("failure")