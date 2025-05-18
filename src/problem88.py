def mystrcmp_ptr(s1: str, s2: str) -> int:
    i = 0
    while True:
        # ������һ�ַ�����β
        if i >= len(s1) or i >= len(s2):
            return len(s1) - len(s2)
        # ���ֲ�ͬ�ַ�
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

    str1 = input("�������һ���ַ���: ")
    str2 = input("������ڶ����ַ���: ")
    
    result_ptr = mystrcmp_ptr(str1, str2)
    print(f"ָ�뷽ʽ�ȽϽ��: {result_ptr}")
    
    result_idx = mystrcmp_idx(str1, str2)
    print(f"�±귽ʽ�ȽϽ��: {result_idx}")

if __name__ == "__main__":
    main()