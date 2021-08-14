def summ(mylist):
    
    if len(mylist) == 1:
        return mylist[0]
    else:
        n = mylist[0]
        mylist.pop(0)
        return n + summ(mylist)

print(summ([1,2,3,120]))