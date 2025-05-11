# 读取输入的数字，以0结束
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

pos = int(input(f"请输入要删除的位置（0-{len(nums)-1}）："))

if 0 <= pos < len(nums):
    del nums[pos]
    print("删除后的数组：", ' '.join(map(str, nums)))
else:
    print("位置不合法，数组保持不变：", ' '.join(map(str, nums)))