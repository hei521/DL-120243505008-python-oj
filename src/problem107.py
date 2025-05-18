class Array:
    def __init__(self):
        self.data = [0.0] * MaxSize  
        self.length = 0  

    def getLength(self):
        return self.length

    def insertX(self, i, x):
        if self.length >= MaxSize:
            raise Exception("Array is full, cannot insert more elements.")
        if i < 0 or i > self.length:
            raise Exception("Invalid index.")

        for j in range(self.length, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.length += 1

    def displayArray(self):
        for i in range(self.length):
            print(self.data[i], end=' ')
        print()

    def deleteAllX(self, x):
        count = 0
        i = 0
        while i < self.length:
            if self.data[i] == x:

                for j in range(i, self.length - 1):
                    self.data[j] = self.data[j + 1]
                self.length -= 1
                count += 1
            else:
                i += 1
        return count

    def mySort(self):

        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.data[i] > self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]


MaxSize = 100

if __name__ == "__main__":
    a = Array()  
    i = 0
    print("���������֣���0�������룩��")
    while True:
        try:
            num = float(input())
            if num == 0:
                break
            a.insertX(i, num)
            i += 1
        except Exception as e:
            print(e)

    print("��ǰ����Ԫ�أ�")
    a.displayArray()

    x = float(input("������Ҫɾ����Ԫ�أ�"))
    n = a.deleteAllX(x)
    print(f"��ɾ�� {n} ��Ԫ��")

    a.mySort()
    print("���������飺")
    a.displayArray()