
nums = []
while True:
    num = int(input("请输入整数（输入0结束）："))
    if num == 0:
        break
    nums.append(num)

if len(nums) >= 100:
    print("警告：输入数字超过100个，将只保留前100个")
    nums = nums[:100]


print("当前数组：", ' '.join(map(str, nums)))

x = int(input("请输入要删除的元素x："))

new_nums = [num for num in nums if num != x]

if len(new_nums) == len(nums):
    print(f"数组中不包含{x}，数组保持不变：", ' '.join(map(str, nums)))
else:
    print(f"删除所有{x}后的数组：", ' '.join(map(str, new_nums)))