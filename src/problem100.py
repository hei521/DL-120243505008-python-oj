class Rectangle:
    def __init__(self, width=10.0, height=10.0):
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height

if __name__ == "__main__":
    w1, h1, w2, h2 = map(float, input().split())
    

    R1 = Rectangle(w1, h1)
    R2 = Rectangle(w2, h2)
    
    area1 = R1.getArea()
    area2 = R2.getArea()

    if area1 > area2:
        print(f"{area1}>{area2}")
    elif area1 < area2:
        print(f"{area1}<{area2}")
    else:
        print(f"{area1}={area2}")