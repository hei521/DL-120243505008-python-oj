
nums = []
while True:
    num = int(input("����������������0��������"))
    if num == 0:
        break
    nums.append(num)

if len(nums) >= 100:
    print("���棺�������ֳ���100������ֻ����ǰ100��")
    nums = nums[:100]


print("��ǰ���飺", ' '.join(map(str, nums)))

x = int(input("������Ҫɾ����Ԫ��x��"))

new_nums = [num for num in nums if num != x]

if len(new_nums) == len(nums):
    print(f"�����в�����{x}�����鱣�ֲ��䣺", ' '.join(map(str, nums)))
else:
    print(f"ɾ������{x}������飺", ' '.join(map(str, new_nums)))