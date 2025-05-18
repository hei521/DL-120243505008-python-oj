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
            print("��������������Ѵﵽ���ޣ�100����")
            break
    
    avg = calculate_average(numbers)
    
    print(f"��{len(numbers)}������ƽ��ֵΪ��{avg:.2f}")

if __name__ == "__main__":
    main()