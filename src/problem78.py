def insert_sorted(arr, x):
    for i in range(len(arr)):
        if x > arr[i]:
            arr.insert(i, x)
            return arr
    arr.append(x)
    return arr

n = int(input())
nums = list(map(int, input(f"������{n}���������ÿո�ָ���").split()))
if len(nums) != n:
        print(f"������Ҫ����{n}������")
else:
        nums_sorted = sorted(nums, reverse=True)
        print("���������飺", ' '.join(map(str, nums_sorted)))
        x = int(input("������Ҫ���������x��"))

        result = insert_sorted(nums_sorted.copy(), x)
        print("���������飺", ' '.join(map(str, result)))