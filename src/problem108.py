class Array:
    def __init__(self, size=100):
        self.maxsize = size
        self.data = [0.0] * self.maxsize  
        self.length = 0

    def __deepcopy__(self, memo):
        new_array = Array(self.maxsize)
        new_array.length = self.length
        new_array.data = self.data.copy() 
        return new_array

    def insertX(self, i, x):
        if self.length >= self.maxsize:
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


def main():
    arr1 = Array() 
    n = 0
    print()
    while True:
        try:
            num = float(input())
            if num == 0:
                break
            arr1.insertX(n, num)
            n += 1
        except Exception as e:
            print(e)

    print("arr1中的元素：", end='')
    arr1.displayArray()

    arr2 = arr1.__deepcopy__({})
    print("arr2中的元素：", end='')
    arr2.displayArray()


if __name__ == "__main__":
    main()