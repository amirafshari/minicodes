# x: profit percentage e.g. 0.2
# fund: initial amount of money
# month: number of months

def f(x, fund, month):
    for i in range(month):
        profit = x*fund
        fund += profit
    return fund

print(f(0.15, 5000000, 12))
