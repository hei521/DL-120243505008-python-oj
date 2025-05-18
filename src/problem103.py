class Cylinder:
    def __init__(self, r, h):
        self.r = r 
        self.h = h  
    
    def getArea(self):
        return 2 * 3.14 * self.r * (self.r + self.h)
    
    def getVolume(self):

        return 3.14 * self.r ** 2 * self.h

if __name__ == "__main__":

    r, h = map(float, input().split())

    cylinder = Cylinder(r, h)
    
    print("表面积：{:.2f}".format(cylinder.getArea()))
    print("体积：{:.2f}".format(cylinder.getVolume()))