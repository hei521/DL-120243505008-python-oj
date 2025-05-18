def mystrcat_ptr(dest: list, src: list) -> list:

    ptr = len(dest)
    dest += [None] * len(src)
    for char in src:
        dest[ptr] = char
        ptr += 1
    return dest

def mystrcat_idx(dest: list, src: list) -> list:
    length = len(dest)
    dest += [None] * len(src)
    for i in range(len(src)):
        dest[length + i] = src[i]
    return dest

def main():
    str1 = list(input("�������һ���ַ���(����<20): ")[:20])
    str2 = list(input("������ڶ����ַ���(����<20): ")[:20])
    
    result_ptr = mystrcat_ptr(str1.copy(), str2)
    print("ʹ��ָ�뷽ʽ���ӽ��:", "".join(result_ptr))
    
    result_idx = mystrcat_idx(str1.copy(), str2)
    print("ʹ���±귽ʽ���ӽ��:", "".join(result_idx))

if __name__ == "__main__":
    main()