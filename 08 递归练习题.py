# 1. 求n的阶乘
# 方法一
def fac(n):
    return 1 if n == 1 else (n * fac(n-1))
print(fac(8))

# 方法二
def fac(n, val=1):
    if n == 1:
        return val
    val = val * n
    return fac(n-1, val)
print(fac(8))

# 2. 将一个数逆序放入列表中，例如1234 => [4,3,2,1]
# 方法一，递归取字符
data = '123456'
def revert(i):
    if i == -1:
        return []
    return [data[i]] + revert(i-1)
print(revert(len(data)-1))
# 方法二，递归切片
def revert(num='12345', target=[]):
    if len(num) == 0:
        return target
    target.append(num[-1])
    return revert(num[:-1])
print(revert())

# 3. 解决猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃了一半，又多吃了一个。
#    以后每天早上都吃了前一天剩下的一半零一个。当到第10天早上想吃时，只剩下一个桃子了。求第一天共摘了多少个桃子。
# 方法一
def peach(day=10):
    if day == 1:
        return 1
    return (peach(day-1)+1) * 2
peach()
# 方法二
def peach(day=1):
    if day == 10:
        return 1
    return (peach(day+1)+1) * 2
peach()
