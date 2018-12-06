#打印字母A
def A():
    for i in range(6):  #控制行
        for k in range(6-i):
            print(" ",end="")
        for j in range(i+1):
            if i ==0 or i ==3 or j==0 or j==i:
                print("* ",end="")
            else:
                 print("  ",end="")
        print()
A()

