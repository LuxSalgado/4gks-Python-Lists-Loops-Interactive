people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    #nuevo = list(filter(lambda x : x != person_name, people))
    nuevo = []
    for x in people:
        if x != person_name:
            nuevo.append(x)
    return nuevo
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))