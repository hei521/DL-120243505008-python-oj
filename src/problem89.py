def insert_char_between(original_str, char_to_insert):
    new_str = char_to_insert.join(original_str[i:i+1] for i in range(len(original_str)))
    return new_str

def main():
    original_str = input("请输入原字符串：")
    char_to_insert = input("请输入要插入的字符：")
    
    result = insert_char_between(original_str, char_to_insert)
    
    print("转换后的新串为：", result)

if __name__ == "__main__":
    main()