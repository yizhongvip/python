# 1. 用户输入一个数字，判断是几位数，打印每一位数字及其重复的次数，依次打印每一位数字，顺序个、十、百、千、万位#
# 输入简单判断
while True:
    num = input(">>>: ").strip().lstrip('0')
    if num.isdigit():
        break

# 判断是几位数字
print("the number of {} length is {}".format(num, len(num)))

# 反向打印每一位数字,方法一
for i in range(len(num)-1, -1, -1):
    print(num[i], end='\t')
print()

# 反向打印每一位数字，方法二
for i in reversed(num):
    print(i, end='\t')
print()
# 计算每一位重复的次数
counter = [0] * 10
for i in num:
    counter[int(i)] += 1

for i in range(len(counter)):
    if counter[i]:
        print("the count of {} is {}".format(i, counter[i]))


# 2. 输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印#
lstNum = []
while len(lstNum) < 5:
    num = input(">>>: ").strip().lstrip('0')
    if not num.isdigit():
        continue
    print("the length of {} is {}".format(num, len(num))) # 打印每个数字的位数
    lstNum.append(num)

print(lstNum)

# sort方法排序
lst = lstNum.copy()
lst.sort()   # 就地修改
print(lst)

# 排序，冒泡法
length = len(lstNum)
for i in range(length-1):
    flag = True
    for j in range(length-i-1):
        if lstNum[j] > lstNum[j+1]:
            tmp = lstNum[j+1]
            lstNum[j+1] = lstNum[j]
            lstNum[j] = tmp
            flag = False
    if flag:
        break
print(lstNum)
