def linearsearch(list1,ele):
    position=0

    while position<len(list1):
        if list1[position]==ele:
            
            position=position+1
        
            print(position)
            break
    else:

        return(None)

list1=[3,6,9,12,30,52]

value=int(input("Enter value to be searched:"))
linearsearch(list1,value)
