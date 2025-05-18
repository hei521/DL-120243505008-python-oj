import math

class Complex:
    def __init__(self, r=0, i=0):
        self.__real = r 
        self.__image = i  

    def displayCom(self):
        if self.__image == 0:
            print(self.__real)
        else:
            print(f"{self.__real}{'+' if self.__image > 0 else ''}{self.__image}i")

    @property
    def real(self):
        return self.__real

    @property
    def image(self):
        return self.__image

    def comAdd(self, other):
        return Complex(self.__real + other.real, self.__image + other.image)

    @classmethod
    def comAdd1(cls, c1, c2):
        return cls(c1.real + c2.real, c1.image + c2.image)

def comAdd2(c1, c2):
    return Complex(c1.real + c2.real, c1.image + c2.image)

def main():
    r1, i1 = map(float, input().split())
    r2, i2 = map(float, input().split())
    c1 = Complex(r1, i1)
    c2 = Complex(r2, i2)
    c3 = Complex()

    c1.displayCom()
    c2.displayCom()
    
 
    c3 = c1.comAdd(c2)
    c3.displayCom()

 
    c3 = Complex.comAdd1(c1, c2)
    c3.displayCom()

    c3 = comAdd2(c1, c2)
    c3.displayCom()

if __name__ == "__main__":
    main()