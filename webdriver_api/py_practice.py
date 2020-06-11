'''
# 迭代
def findMaxAndMin(L):
    x_max = L[0]
    x_min = L[0]
    for i in L:
        if i >= x_max:
            x_max = i
        if i < x_min:
            x_min = i
    return(x_max,x_min)

# 列表生成式
L1 = ['Hello','World',18,'Apple',None]

L2 = [s.lower() if isinstance(s,str) else str(s).lower() for s in L1]
# 高阶函数map的应用
def normalize(name):
    def changesize(s):
        my_str = ''
        for i in s:
            if i == s[0]:
                i = i.upper()
            else:
                i = i.lower()
            my_str = my_str + i
        return my_str
    return map(changesize,name)
L1 = ['adam','LISA','barT']
L2 = list(normalize(L1))
print(L2)

# 高阶函数reduce
from functools import reduce

def prod(L):
    def multiply(x,y):
        return x*y
    return(reduce(multiply,L))
L = [3,5,7,9]
print(prod(L))

# 上面函数的lambda写法
from functools import reduce
def prod(L):
    return(reduce(lambda x, y:x*y, L))
L = [3,5,7,9]
print(prod(L))

# map和reduce的组合应用，将字符串转换为浮点数
from functools import reduce
def str2float(s):
    my_list = s.split('.')
    n = len(my_list[1])
    
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9,}
    def char2num(k):
        return DIGITS[k]
    def fn(x,y):
        return x * 10 + y
    def str2int(my_str):
        return reduce(fn,map(char2num,my_str))
    return str2int(my_list[0]) + (str2int(my_list[1]))*10**(-n)
print(str2float('123.456'))
print(str2float('4321.123456789'))


# 用filter筛选回数
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
output = filter(is_palindrome,range(1,1000))
print('1-1000',list(output))
print(list(filter(is_palindrome,range(1,200))

# sorted函数练习
def by_name(t):
    return t[0].upper()
def by_score(t):
    return t[1]
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)
'''
# 使用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    def num_generator():
        n = 0
        while True:
            n = n + 1
            yield n
    num = num_generator()
    def counter():
        return next(num)
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
