class CString:
    def __init__(self, s=""):
        self.__str = s 
    
    def displayString(self):
        print(f"String: {self.__str}")
    
    def mystrlen(self):
        return len(self.__str)
    
    def __deepcopy__(self, memo):
        return CString(self.__str)

def main():

    input_str = input("Enter a string: ")

    S1 = CString(input_str)
    print("S1 Info:")
    S1.displayString()
    print(f"Length: {S1.mystrlen()}")
    
    S2 = S1.__deepcopy__({})
    print("\nS2 Info (created by copy constructor):")
    S2.displayString()

if __name__ == "__main__":
    main()