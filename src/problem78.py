def insert_sorted(arr, x):
    for i in range(len(arr)):
        if x > arr[i]:
            arr.insert(i, x)
            return arr
    arr.append(x)
    return arr

n = int(input())
nums = list(map(int, input(f"请输入{n}个整数，用空格分隔：").split()))
if len(nums) != n:
        print(f"错误：需要输入{n}个整数")
else:
        nums_sorted = sorted(nums, reverse=True)
        print("排序后的数组：", ' '.join(map(str, nums_sorted)))
        x = int(input("请输入要插入的整数x："))

        result = insert_sorted(nums_sorted.copy(), x)
        print("插入后的数组：", ' '.join(map(str, result)))