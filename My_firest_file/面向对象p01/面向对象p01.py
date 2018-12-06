import  random
import  math

"""
输入一个三位随机数比较大小
若大于随机数，则分别输出这三位数的个位十位百位输出
若等于，则提示中奖记 100分
若小于则将120个字符输入到文本文件中
（规则是每一条字符串场12，单独占一行并且前四个是字母，后8个是数字）
"""
def line():
    str_num = ""
    for i in range(4):
        num = random.randrange(97,123)
        str_s = chr(num)
        str_num = str_num+str_s
    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num+str(num)
    return str_num
source = 0
total = 0
def num_game(source,total):
    while 1:
        num = input("请输入一个随机数,输入-1结束：")
        if num == "-1":
            break
        random_num = random.randrange(100,1000)
        if num.isdigit() and 100<=int(num) <=999:
            total+=1
            print("有效输入%d次"%total)
            num = int(num)
            if num > random_num:
                bai = num //100
                shi = (num %100)//10
                ge = num%10
                print("你输入的数字比程序随机数大，程序随机数是{}".format(random_num))
                print("这个三位数的个位数是{}十位是{}百位是{}".format(ge,shi,bai))
            if num  == random_num:
                source +=10

                print("你中奖了，目前的分数是{}".format(source))
            if num  < random_num:
                print("你输入的数字比程序随机数小，程序随机数是{}".format(random_num))
                for i in range(10):
                    str_line = line()
                    print(str_line)
                    with open("str_num.txt","a")as f:
                        f.write(str_line+"\n")
        else:
            print("请输入数字")
#程序入口
if __name__=="__main__":
    source = 0
    total = 0
    num_game(source,total)