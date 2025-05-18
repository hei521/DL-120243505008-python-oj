class Person:
    def __init__(self, name, id_num):
        self.name = name 
        self.id = id_num
    
    def __copy__(self):
        return Person(self.name, self.id)
    
    def display_person(self):
        print(f"姓名：{self.name}，身份证号：{self.id}")
    

    def __del__(self):
        print(f"释放 {self.name} 的资源")

def main():
    p1 = Person("张三", 123456)
    
    p2 = p1.__copy__()
    p1.display_person()
    p2.display_person()

if __name__ == "__main__":
    main()