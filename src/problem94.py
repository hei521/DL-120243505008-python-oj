def calculate_average(arr):
    if len(arr) == 0:
        return 0.0  
    return sum(arr) / len(arr)

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
    
    avg = calculate_average(numbers)
    
    print(f"这{len(numbers)}个数的平均值为：{avg:.2f}")

if __name__ == "__main__":
    main()