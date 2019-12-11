################## 1. 求100内所有奇数的和（2500） ##################
# 方法一
num = 100
s = 0

for i in range(num):
    if i % 2:
        s += i
print(s)

# 方法二
num = 100
s = 0

for i in range(1, num, 2):  # 减少迭代次数，提高程序执行效率
    s += i
print(s)


################## 2. 判断学生成绩，成绩等级A-E。其中，90分以上为A，80-89分为B，70-79分为C，60-69分为D，60以下为E ##################
score = int(input(">>: "))

if score >= 70:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")
else:
    if score >= 60:
        print("D")
    else:
        print("E")


################## 3. 打印一个边长为n的正方形 ##################
n = int(input(">>: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " "*(n-2) + "*")

################## 4.求1到n的阶乘之和 ##################
# 方法一：使用两次循环
he = 0
n = int(input(">>>: "))
for i in range(n, 0, -1):
 ji = 1
 for j in range(i, 0, -1):
    ji *= j
 he += ji

print(he)

# 方法二：只使用一次循环，提高效率
s = 0
val = 1
n = int(input(">>>: "))
for i in range(1, n+1):
    val *= i
    s += val
print(s)

################## 5. 给一个数，判断他是否是素数（质数），质数：一个大于1的自然数只能被1和他本身整除 ##################
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

################## 6. 给一个半径，求圆的面积和周长。圆周率3.14 ##################
r = float(input(">>>: "))
pi = 3.14
area = pi * (r ** 2)
perimeter = 2 * pi * r
print("area:", area, "perimeter:", perimeter)


################## 7. 输入两个数，比较大小后，从小到大升序打印 ##################
num1 = int(input(">>>: "))
num2 = int(input(">>>: "))

if num1 >= num2:
    print(num2, num1)
else:
    print(num1, num2)

################## 8. 获取最大值，依次输入若干个整数，打印出最大值，输入为空，则退出程序 ##################
maxNum = input(">>>: ")

if max != "":
    maxNum = int(maxNum)
    while True:
        num = input(">>>: ")
        if num == "":
            break
        num = int(num)
        if num > maxNum:
            maxNum = num
            print(maxNum)


################## 9. 输入n个数，求每次输入后的算数平均数 ##################
count = 0
numSum = 0

while True:
    num = input(">>>:")
    if num == "":
        break
    num = int(num)
    count += 1
    numSum += num
    print("avg is: ", numSum/count)

################## 10. 打印九九乘法表 ##################
# 方法一：print函数打印
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", i*j, sep="", end="\t")
    print()

# 方法二：format函数格式化输出打印
for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}*{1}={2}".format(j, i, j*i), end="\t")
    print()


################## 11. 打印如下菱形 ################## 3 2 1 0
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
n = int(input(">>>: "))
e = n//2

for i in range(-e, e+1):
    x = -i if i < 0 else i
    print(" " * x + "*" * (n - 2*x))

################## 12. 解决猴子吃桃问题 ##################
# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃了一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想吃时，只剩下一个桃子了。求第一天共摘了多少个桃子。
peach = 1
for _ in range(9):
    peach = 2 * (peach + 1)
print(peach)

##################### 13. 给定一个不超过5位的正整数，判断该数的位数，依次打印出万位、千位、百位、十位、个位的数字 #####################
# 思路：每一趟中，整除就能获得最高位的数字，取模就能获得除去最高位的数的剩余数字，且取模后的数字作为下下一趟的整除数字
x = 54321
w = 10000

for i in range(5):
    y = x // w
    x = x % w
    w //= 10
    print(y)

##################### 14. 给定一个不超过5位的正整数，判断该数的位数，依次打印出个位、十位、百位、千位、万位的数字 #####################
num = int(input("输入一个正整数： "))
n = 5
if num >= 1000: # 折半,判断该数有几位
    if num >= 10000:
        n = 5
    else:
        n = 4
else:
    if num >= 100:
        n = 3
    elif num >= 10:
        n = 2
    else:
        n = 1

for i in range(n):
    print(num % 10)
    num //= 10

##################### 15. 求100内所有奇数的和（2500） #####################
# 方法一
num = 100
s = 0

for i in range(num):
    if i % 2:
        s += i
print(s)

# 方法二
num = 100
s = 0

for i in range(1, num, 2):  # 减少迭代次数，提高程序执行效率
    s += i
print(s)

##################### 16. 打印100以内的斐波那契数列 #####################
# 斐波那契数列：后一项的值等于前两项之和，如：1，1，2，3，5，8，13，21，34，55
a = 0
b = 1
print(a, b, end=" ")

while True:
    c = a + b
    if c > 100:
        break
    print(c, end=" ")
    a = b
    b = c

##################### 17. 求斐波那契数列第101项 #####################
a = 0
b = 1
index = 2

while True:
    c = a + b
    if index == 101:
        print(index, c, end=" ")
        break
    a = b
    b = c
    index += 1

##################### 18. 求10万内的所有素数 #####################
# 方法一
n = 100000
for i in range(3, n, 2):
    flag = True
    for j in range(2, i):
        if not i % j:
            flag = False
            break
    if flag:
        print(i, end=" ")

# 方法二，优化一
n = 100000
print(2)
count = 1
for i in range(3, n, 2):
    for j in range(2, int(i**0.5) + 1):
        if not i % j:
            break
    else:
        #print(i)
        count += 1
print(count)

# 方法三，优化二
n = 100000
# print(2)
count = 1
for i in range(3, n, 2): # 舍弃掉所有偶数
    if i > 10 and i % 5 == 0: # 所有大于10的质数中，个位数只有1，3，7，9.意思是大于5，结尾是5就能被5整除了
        continue
    for j in range(3, int(i**0.5) + 1, 2): # 为什么从3开始，步长为2？既然没有偶数了，就没必要和2取模了，因为奇数%偶数一定不能整除
        if not i % j:
            break
    else:
        #print(i)
        count += 1
print(count)






