arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(items):
    odds = 0
    for x in items:
        if (x % 2 != 0):
            odds = odds + x
    return odds

print(sumOdds(arr))

