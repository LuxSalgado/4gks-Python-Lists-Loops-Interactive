chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    nuevo = []
    for x in list1:
        nuevo.append(x)
    for x in list2:
        nuevo.append(x)
    return nuevo
    
print(merge_list(chunk_one, chunk_two))
