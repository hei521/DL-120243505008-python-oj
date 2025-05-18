class Person:
    def __init__(self, name, id_num):
        self.name = name  
        self.id = id_num
    
    def Display(self):
        print(f"name:{self.name} id:{self.id}")
    
    def __del__(self):
        pass 

class CollegeStu(Person):
    def __init__(self, name, id_num, major, score):
        super().__init__(name, id_num) 
        self.major = major  
        self.score = score
    
    def Display(self):
        print(f"major:{self.major} score:{self.score:.1f}")
    
    def __del__(self):
        pass  

def main():
    import sys
    input_line = sys.stdin.readline().strip().split()
    name = input_line[0]
    id_num = int(input_line[1])
    major = input_line[2]
    score = float(input_line[3])
    cs = CollegeStu(name, id_num, major, score)
    cs.Person.Display()  # 输出姓名，id
    cs.Display()    # 输出专业、成绩

if __name__ == "__main__":
    main()