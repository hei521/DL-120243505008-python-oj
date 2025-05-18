def binary_to_decimal(binary_str):
    decimal = 0
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)
    return decimal

def main():
    n = int(input("请输入二进制数的个数n："))
    if n >= 100:
        print("n必须小于100")
        return
    
    total = 0
    for i in range(n):
        binary_str = input(f"请输入第{i+1}个二进制数：")
        decimal = binary_to_decimal(binary_str)
        total += decimal
    
    print(f"{n}个二进制数的和为：{total}（十进制）")

if __name__ == "__main__":
    main()