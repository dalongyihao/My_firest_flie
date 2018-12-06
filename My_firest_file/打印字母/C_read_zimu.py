def C():
    for i in range(4):
        for j in range(3):
            if j==0:
                if i == 1 or i == 2:
                    print("* ", end="")
                else:
                    print("  ", end="")
            elif i == 0 or i == 3  :
                print("* ", end="")
            else:
                print("  ", end="")
        print()
C()