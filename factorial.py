def fact(x):
    n = 1
    while x != 1:
        n *= x
        x -= 1
    return n


# Recursive
def facto(x):
    if x == 1:
        return 1
    else:
        return x*facto(x-1)