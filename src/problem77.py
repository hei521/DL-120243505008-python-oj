
nums = []
while True:
    num = int(input("������һ������������0��������"))
    if num == 0:
        break
    nums.append(num)

if len(nums) >= 100:
    print("��������ֳ���100������ֻ����ǰ100��")
    nums = nums[:100]

pos = int(input("���������λ�ã�0��{}����".format(len(nums))))
x = int(input("������Ҫ�����Ԫ�أ�"))


if pos < 0 or pos > len(nums):
    print("����λ�ò��Ϸ�")
else:
    nums.insert(pos, x)
    print("���������飺", ' '.join(map(str, nums)))