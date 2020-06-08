from functools import reduce
def str2float(s):
    my_list = s.split('.')
    
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9,}
    def char2num(k):
        return DIGITS[k]
    def fn(x,y):
        return x * 10 + y
    def str2int(my_str):
        return reduce(fn,map(char2num,my_str))
    return str2int(my_list[0]), str2int(my_list[1]),len(my_list[1])
print(str2float('123.456')) 
