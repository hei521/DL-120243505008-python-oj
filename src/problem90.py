def binary_to_decimal(binary_str):
    decimal = 0
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)
    return decimal

def main():
    n = int(input("��������������ĸ���n��"))
    if n >= 100:
        print("n����С��100")
        return
    
    total = 0
    for i in range(n):
        binary_str = input(f"�������{i+1}������������")
        decimal = binary_to_decimal(binary_str)
        total += decimal
    
    print(f"{n}�����������ĺ�Ϊ��{total}��ʮ���ƣ�")

if __name__ == "__main__":
    main()