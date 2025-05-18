def convert_with_index(s):
    converted = list(s)
    for i in range(len(converted)):
        char = converted[i]
        if 'A' <= char <= 'Z':
            converted[i] = char.lower()
        elif 'a' <= char <= 'z':
            converted[i] = char.upper()
    return ''.join(converted)

def convert_with_pointer(s):

    converted = []
    for char in s:
        if 'A' <= char <= 'Z':
            converted.append(char.lower())
        elif 'a' <= char <= 'z':
            converted.append(char.upper())
        else:
            converted.append(char)
    return ''.join(converted)

def main():

    input_str = input()
    
    if len(input_str) > 99:
        print("错误：字符串长度超过99")
        return
    
    result_index = convert_with_index(input_str)
    print("使用下标方式转换结果:", result_index)
    
    result_pointer = convert_with_pointer(input_str)
    print("使用指针方式转换结果:", result_pointer)

if __name__ == "__main__":
    main()