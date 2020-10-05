def linearsearch(list1,ele):
    position=0

    while position<len(list1):
        if list1[position]==ele:
            
            position=position+1
        
            print(position)
            break
    else:

        return(None)

list1=[3,6,9,22,40,62]

value=int(input("Enter value to be searched:"))
linearsearch(list1,value)
'''

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
#main--
number=int(input("enter a no.:"))
factorial(number)
'''