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
    str1 = list(input("请输入第一个字符串(长度<20): ")[:20])
    str2 = list(input("请输入第二个字符串(长度<20): ")[:20])
    
    result_ptr = mystrcat_ptr(str1.copy(), str2)
    print("使用指针方式连接结果:", "".join(result_ptr))
    
    result_idx = mystrcat_idx(str1.copy(), str2)
    print("使用下标方式连接结果:", "".join(result_idx))

if __name__ == "__main__":
    main()