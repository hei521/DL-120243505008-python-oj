# ��ȡ��������֣���0����
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

pos = int(input(f"������Ҫɾ����λ�ã�0-{len(nums)-1}����"))

if 0 <= pos < len(nums):
    del nums[pos]
    print("ɾ��������飺", ' '.join(map(str, nums)))
else:
    print("λ�ò��Ϸ������鱣�ֲ��䣺", ' '.join(map(str, nums)))