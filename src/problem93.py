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
            print("��������������Ѵﵽ���ޣ�100����")
            break

    x = int(input("������Ҫ���ҵ�����x��"))

    index = find_first_index(numbers, x)
    
    print(f"���ҽ����{index}")

if __name__ == "__main__":
    main()