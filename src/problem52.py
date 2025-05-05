def f(a):
    if a < 4:
        return 1
    else:
        return f(a-1)+f(a-3)
 
a=int(input())
print(f(a))