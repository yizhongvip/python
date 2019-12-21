############### 1. 用户输入一个数字，打印每一位数字及其重复的次数 ###############
num = input(">>>: ")
counter = {}
for i in num:
    # 1. 方法一
    # if i not in counter.keys():
    #     counter[i] = 0
    # counter[i] += 1
    
    # 2. 方法二
    # counter[i] = counter.get(i, 0) + 1
    
    # 3. 方法三
    counter[i] = counter.setdefault(i, 0) + 1
print(counter)

############## 2. 数字重复统计 ###############
# 随机产生100个整数
# 数字的范围[-1000, 1000]
# 升序输出这些数字并打印其重复的次数
import random
nums = []
counter = {}
for _ in range(100):
    nums.append(random.randrange(-1000, 1000))
print(nums)
# 统计数字重复的次数
for c in nums:
    counter[c] = counter.get(c, 0) + 1
# 1. sorted来排序，sorted是内建函数
newdict = sorted(counter.items())
print(newdict)
# 2. 使用list的sort函数
keys = list(counter.keys())
for k in keys:
    print((k, counter[k]))

############### 3. 字符串重复统计 ###############
# 字符表'abcdefghijklmnopqrstuvwxyz'
# 随机挑选2个字母组成字符串，共挑选100个
# 降序输出所有不同的字符串及重复的次数
import random
s = 'abcdefghijklmnopqrstuvwxyz'
counter = {}
# 挑选100个随机由2个字母组成的字符串
words = [random.choice(s) + random.choice(s) for _ in range(100)]
# 统计字符串重复的次数
for word in words:
    counter[word] = counter.get(word, 0) + 1
# 降序输出所有不同的字符串
print(sorted(counter.items(), reverse=True))
