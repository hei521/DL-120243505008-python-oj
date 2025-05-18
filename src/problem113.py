class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    
    def setCom(self, real, imag):
        self.real = real
        self.imag = imag
    
    def displayCom(self):
        print(f"Complex({self.real},{self.imag})")


def main():
    import sys
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    r1, i1 = map(float, input_lines[0].split())
    r2, i2 = map(float, input_lines[1].split())
    
    c1 = Complex(r1, i1)
    c2 = Complex()
    
    c1.displayCom()
    c2.displayCom()
    
    c2.setCom(r2, i2)
    c2.displayCom()

if __name__ == "__main__":
    main()