
nums = []
while True:
    num = int(input("请输入一个整数（输入0结束）："))
    if num == 0:
        break
    nums.append(num)

if len(nums) >= 100:
    print("输入的数字超过100个，将只保留前100个")
    nums = nums[:100]

pos = int(input("请输入插入位置（0到{}）：".format(len(nums))))
x = int(input("请输入要插入的元素："))


if pos < 0 or pos > len(nums):
    print("插入位置不合法")
else:
    nums.insert(pos, x)
    print("插入后的数组：", ' '.join(map(str, nums)))