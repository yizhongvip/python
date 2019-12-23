# 以下题目要求使用列表解析式完成
############### 1. 返回1-10平方的列表 ###############
lst = [(i+1)**2 for i in range(10)]
print(lst)

############### 2. 有一个列表lst=[1,4,9,16,2,5,10,15]，生成一个新列表，要求新列表元素是lst相邻2项的和 ###############
lst=[1, 4, 9, 16, 2, 5, 10, 15]
newlst = [lst[i] + lst[i+1] for i in range(len(lst)-1)]
print(newlst)

############### 3. 打印九九乘法表 ###############
[print('{0}*{1}={2}'.format(j, i, j*i), end='\t' if i != j else '\n') for i in range(1, 10) for j in range(1, i+1)]

############### 4. "0001.abadicddws","0002.xyzikqhujl","0003.ihnilmeila"是ID格式，要求ID格式是以点号分割，
# 左边是4位从1开始的整数，右边是10位随机小写英文字母。请依次生成前100个ID的列表 ###############
import random
words = 'abcdefghijklmnopqrstuvwxyz'

lst = ['{:04}.{}'.format(i, ''.join(random.choices(words, k=10))) for i in range(1, 101)]
print(lst)
