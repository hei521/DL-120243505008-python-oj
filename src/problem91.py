def move(numbers):
    return numbers[-3:] + numbers[:-3]

def main():
    n = int(input("��������������n(3<=n<=10)��"))
    if n < 3 or n > 10:
        print("n������3��10֮��")
        return
    
    numbers = []
    for i in range(n):
        num = int(input(f"�������{i+1}��������"))
        numbers.append(num)
    result = move(numbers)
    print("�ƶ���Ľ��Ϊ��", end="")
    for num in result:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()