from random import randint

def bin_search(lst,item):
    mid = len(lst) - 1
    low = 0
    high = len(lst) - 1
    while lst[mid] != item and low<=high:
        if item > lst[mid]:
            low = mid +1
        else:
            high = mid -1
        mid = (low+high)//2
    if low > high :
        return None
    else :
        return mid

a=[]
for i in range(10):
    a.append(randint(1,20))
a.sort()
print(a)
value = int(input("enter value to be searched:"))
print("Element found at index:",bin_search(a,value))




