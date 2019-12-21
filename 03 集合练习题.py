# 随机产生2组各10个数字的列表，要求如下:
# 每个数字取值范围[10, 20]
# 统计20个数字中，一共有多少个不同的数字？
# 2组之间进行比较，不重复的数字有几个？分别是什么？
# 2组之间比较，重复的数字有几个？分别是什么？

import random
lst1 = []
lst2 = []
# 随机产生2组各10个数字的列表
for _ in range(10):
    lst1.append(random.randint(10, 20))
    lst2.append(random.randint(10, 20))

set1 = set(lst1)
set2 = set(lst2)

# 统计20个数字中，一共有多少个不同的数字？
print("不同的数字共有{}个".format(set1.union(set2)))
# 2组之间进行比较，不重复的数字有几个？分别是什么？
print("不重复的数字{}".format(set1.symmetric_difference(set2)))
# 2组之间比较，重复的数字有几个？分别是什么？
print("重复的数字{}".format(set1.intersection(set2)))
