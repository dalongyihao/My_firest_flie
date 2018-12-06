
def B():
    for i in range(3):
        for j in range(4):
            if i==0 or i ==3 or j ==0 :
                if j <3:
                    print("* ",end="")
            elif j==3:
                if i==1 or i ==2:
                    print("* ", end="")
            else:
                print("  ",end="")
        print()
    for i in range(4):
        for j in range(4):
            if i==0 or i ==3 or j ==0 :
                if j <3:
                    print("* ",end="")
            elif j==3:
                if i==1 or i ==2:
                    print("* ", end="")
            else:
                print("  ",end="")
        print()
