# 1. 取出列表下面列表的第二个、第四个、倒数第二个
lst = list(range(10))
_, a, _, b, *_, c, _ = lst
print(a, b, c)

# 2. 从lst = [1, (2, 3, 4), 5]中，提取4出来
lst = [1, (2, 3, 4), 5]
_, (*_, a), _ = lst
print(a)

# 3. 环境变量JAVA_HOME=/usr/bin，返回环境变量名和路径
# 方法一
env, path = 'JAVA_HOME=/usr/bin'.split(sep='=',maxsplit=1)
print(env, path)
# 方法二
env, _, path = 'JAVA_HOME=/usr/bin'.partition('=')
print(env,path)

# 4. 对列表[1, 9, 8, 5, 6, 7, 4, 3, 2]使用冒泡法排序，要求使用封装和解构来交换数据
nums = [1, 9, 8, 5, 6, 7, 4, 3, 2]
length = len(nums)
for i in range(length - 1):
    flag = True
    for j in range(length - i -1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = False
    if flag:
        break
print(nums)
