def binary(item, mylist):
    low = 0
    high = len(mylist)
    i = 0
    
    while low <= high:
        mid = (low + high)//2
        guess = mylist[mid]
        i+=1
        

        if guess == item:
            return (guess, i)
        if guess > item:
            high = mid
        else:
            low = mid
    return None


print(binary(97, [i for i in range(5000)]))