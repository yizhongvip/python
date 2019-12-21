##################### 1. 求100内的素数 #####################
# 从2开始到自身的-1的数中找到一个能整除的，从2开始到自身开平方的数中找到一个能整除的
# 一个合数一定可以分解成几个素数的乘积，也就是说，一个数如果能够被一个素数整除就是合数
# 方法一
# prime = []
# prime.append(2)
# for i in range(3, 100, 2):
#     for j in range(3, int(i**0.5) + 1, 2):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
# print(prime)

# 方法二，不推荐
# prime = []
# for i in range(2, 100):
#     for j in prime: # 奇数都多，质数列表
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
# print(prime)

# 方法三
# prime = []
# for x in range(2, 100):
#     flag = False # 不是合数
#     edge = x ** 0.5
#     for i in prime:
#         if x % i == 0: # 找到了合数x
#             flag = True # 合数
#             break
#         if i > edge: # 找到了质数x
#             break
#     if not flag: # 找到了质数x
#         prime.append(x)
#
# print(prime)

# 方法四，大于3的素数只有6N-1和6N+1两种形式
count = 2
n = 100
x = 5
step = 2
while x <= n:
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            break
    else:
        count += 1

    x += step
    step = 4 if step == 2 else 2
print(count)




##################### 2. 计算杨辉三角前6行（只要求打印杨辉三角的数字即可） #####################
# 第n行有n项，n是正整数
# 第n行数字之和为2 ** (n-1)




##################### 3. 依次接收用户输入的3个数，排序后打印 #####################
# 1）使用分支结构完成
# nums = []
# out = None
#
# for _ in range(3):
#     nums.append(int(input(">>>: ")))
#
# if nums[0] > nums[1]:
#     if nums[0] > nums[2]:
#         if nums[1] > nums[2]:
#             out = [2, 1, 0]
#         else:
#             out[1, 2, 0]
#     else: # nums[2]>nums[0]
#         out = [1, 0, 2]
# else: # nums[1]>nums[0]
#     if nums[1] > nums[2]:
#         if nums[0] > nums[2]:
#             out = [2, 0, 1]
#         else:
#             out = [0, 2, 1]
#     else:
#         out = [0, 1, 2]
#
# for i in out:
#     print(nums[i], end="\t")


# 2）使用max函数，效率低，不推荐
# nums = []
# out = None
#
# for _ in range(3):
#     nums.append(int(input(">>>: ")))
#
# while nums:
#     if len(nums) == 1:
#         print(nums[0])
#         break
#     m = max(nums)
#     print(m, end="\t")
#     nums.remove(m)

# 3） 使用列表的sort方法
# nums = []
#
# for _ in range(3):
#     nums.append(int(input(">>>: ")))
#
# nums.sort()
# print(nums)


# 4） 排序算法，冒泡排序
# 冒泡法需要数据一轮轮比较
# 可以假定一个标记判断此轮是否有数据交换发生，如果没有发生交换，可以结束排序，如果发生交换，继续下一轮排序
# 最差的排序情况是，初始顺序与目标顺序完全相反，遍历次数1，...，n-1之和n(n-1)/2
# 最好的排序情况是，初始顺序与目标顺序完全相同，遍历次数n-1
# 时间复杂度O(n**2)
# nums = [44, 66, 55, 99, 33, 88, 120, 11, 122, 1, 134, 77]
# length = len(nums)
# for i in range(length-1):
#     flag = True
#     for j in range(0, length-i-1):
#         if nums[j] > nums[j+1]: # 升序，改成<号，则为降序
#             flag = False # 如果没有发生交换，则没有必要再进行下面的比较
#             tmp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = tmp
#     if flag:
#         break
# print(nums)

# 5）选择排序






# 6）插入排序


