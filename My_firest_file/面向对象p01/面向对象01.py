import random
import math
def sjhs():
    num = input("请输入一个1,2,3三个数字：")
    rand_num =random.randrange(1,4)
    num = int(num)
    source = 0
    if num > rand_num:
        print("输入的数字比随机数大")
    elif num == rand_num:
        source +=100
        print(source)
    elif num < rand_num:
         print("输入的数字比随机数小")
    return sjhs()
