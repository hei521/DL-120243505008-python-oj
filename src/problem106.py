class Array:
    def __init__(self):
        self.data = [0.0] * 100  
        self.length = 0  
    def getLength(self):
        return self.length

    def insertX(self, i, x):
        if self.length >= 100:
            print("Array is full, cannot insert more elements.")
            return
        if i < 0 or i > self.length:
            print("Invalid index.")
            return
       
        for j in range(self.length, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.length += 1

    def displayArray(self):
        for i in range(self.length):
            print(self.data[i], end=' ')
        print()

def main():
    arr = Array()
    print("�����������˫���ȸ���������0�������룩��")
    while True:
        x = float(input())
        if x == 0:
            break
        arr.insertX(arr.getLength(), x) 
    print("�����е�Ԫ��Ϊ��")
    arr.displayArray()


if __name__ == "__main__":
    main()