def find_first_index(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    numbers = []
    print()
    while True:
        num = int(input())
        if num == 0:
            break
        numbers.append(num)
        if len(numbers) >= 100:
            print("输入的整数个数已达到上限（100个）")
            break

    x = int(input("请输入要查找的整数x："))

    index = find_first_index(numbers, x)
    
    print(f"查找结果：{index}")

if __name__ == "__main__":
    main()