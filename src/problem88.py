def mystrcmp_ptr(s1: str, s2: str) -> int:
    i = 0
    while True:
        # 到达任一字符串结尾
        if i >= len(s1) or i >= len(s2):
            return len(s1) - len(s2)
        # 发现不同字符
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])
        i += 1

def mystrcmp_idx(s1: str, s2: str) -> int:
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])

    return len(s1) - len(s2)

def main():

    str1 = input("请输入第一个字符串: ")
    str2 = input("请输入第二个字符串: ")
    
    result_ptr = mystrcmp_ptr(str1, str2)
    print(f"指针方式比较结果: {result_ptr}")
    
    result_idx = mystrcmp_idx(str1, str2)
    print(f"下标方式比较结果: {result_idx}")

if __name__ == "__main__":
    main()