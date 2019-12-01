# 1. 求100内所有奇数的和（2500）
# 方法一
# num = 100
# s = 0
#
# for i in range(num):
#     if i % 2:
#         s += i
# print(s)

# 方法二
# num = 100
# s = 0
#
# for i in range(1, num, 2):  # 减少迭代次数，提高程序执行效率
#     s += i
# print(s)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 2. 判断学生成绩，成绩等级A-E。其中，90分以上为A，80-89分为B，70-79分为C，60-69分为D，60以下为E
# score = int(input(">>: "))
#
# if score >= 70:
#     if score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     else:
#         print("C")
# else:
#     if score >= 60:
#         print("D")
#     else:
#         print("E")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 3. 打印一个边长为n的正方形
# n = int(input(">>: "))
#
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print("*" * n)
#     else:
#         print("*" + " "*(n-2) + "*")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 4.求1到n的阶乘之和
# 方法一：使用两次循环
# he = 0
# n = int(input(">>>: "))
# for i in range(n, 0, -1):
# 	ji = 1
# 	for j in range(i, 0, -1):
# 		ji *= j
# 	he += ji

# print(he)

# 方法二：只使用一次循环，提高效率
# s = 0
# val = 1
# n = int(input(">>>: "))
# for i in range(1, n+1):
#     val *= i
#     s += val
# print(s)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 给一个数，判断他是否是素数（质数），质数：一个大于1的自然数只能被1和他本身整除
num = int(input(">>>: "))
flag = True

for i in range(2, num):
    if not num % i:
        flag = False
        break
if flag:
    print(str(num) + "是质数")
else:
    print(str(num) + "不是质数")