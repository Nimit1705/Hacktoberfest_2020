with open("stu_record.txt","r") as fw:
    countdigit=0
    countupper=0
    countlower=0
    for line in fw:
        for i in line:
            if i.isdigit():
                countdigit+=1
            if i.islower():
                countlower+=1
            if i.isupper():
                countupper+=1
    print("No of digit:",countdigit)
    print("No of lower case letter:",countlower)
    print("No of upper case letter:",countupper)                    

