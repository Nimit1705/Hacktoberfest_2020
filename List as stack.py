s=[]
c="y"
while(c=="y"):
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        a=input("Enter any number:")
        s.append(a)
    elif (choice==2):
        if (s==[]):
            print("Stack empty")
        else:
            print("Deleted elements is:",s.pop())
    elif (choice==3):
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])

    else:
        print("WRONG INPUT!!!")
    c=input("Do you want to continue or not? ")            
                        