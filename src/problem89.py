def insert_char_between(original_str, char_to_insert):
    new_str = char_to_insert.join(original_str[i:i+1] for i in range(len(original_str)))
    return new_str

def main():
    original_str = input("������ԭ�ַ�����")
    char_to_insert = input("������Ҫ������ַ���")
    
    result = insert_char_between(original_str, char_to_insert)
    
    print("ת������´�Ϊ��", result)

if __name__ == "__main__":
    main()