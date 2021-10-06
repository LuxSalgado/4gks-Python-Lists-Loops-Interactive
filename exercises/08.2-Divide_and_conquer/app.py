list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(numeros):
    odd = []
    even = []
    for x in numeros:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x) 
    juntos = []
    juntos.append(odd)
    juntos.append(even)
    return juntos


print(merge_two_list(list_of_numbers))

