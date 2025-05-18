def move(numbers):
    return numbers[-3:] + numbers[:-3]

def main():
    n = int(input("请输入整数个数n(3<=n<=10)："))
    if n < 3 or n > 10:
        print("n必须在3到10之间")
        return
    
    numbers = []
    for i in range(n):
        num = int(input(f"请输入第{i+1}个整数："))
        numbers.append(num)
    result = move(numbers)
    print("移动后的结果为：", end="")
    for num in result:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()