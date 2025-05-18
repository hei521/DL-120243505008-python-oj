class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    
    def displayComplex(self):
        output = []

        if self.real != 0 or self.imag == 0:
            output.append(f"{self.real}")
        

        if self.imag != 0:
            if self.imag == 1:
                output.append("+i" if len(output) > 0 else "i")
            elif self.imag == -1:
                output.append("-i")
            else:
                sign = "+" if self.imag > 0 and len(output) > 0 else ""
                output.append(f"{sign}{self.imag}i")
        

        result = "".join(output)
        

        if not output: 
            print("0")
        elif self.real == 0 and self.imag != 0: 
            print(result.lstrip("+"))
        else:
            print(result)


if __name__ == "__main__":
    r1, i1 = map(float, input().split())
    c1 = Complex(r1, i1)
    c1.displayComplex()