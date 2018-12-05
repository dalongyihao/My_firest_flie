import  random
import  math

"""
输入一个三位随机数比较大小
若大于随机数，则分别输出这三位数的个位十位百位输出
若等于，则提示中奖记 100分
若小于则将120个字符输入到文本文件中
（规则是每一条字符串场12，单独占一行并且前四个是字母，后8个是数字）
"""
num = input("请输入一个随机数：")
random_num = random.randrange(100,1000)
if num.isdigit() and 100<=int(num) <=999:
    num = int(num)
    if num > random_num:
        bai = num //100
        shi = (num %100)//10
        ge = num%10
        print("这个三位数的个位数是{}十位是{}百位是{}".format(ge,shi,bai))
    if num  == random_num:
        pass
    if num  < random_num:
        print(random_num)
else:
    print("请输入数字")
