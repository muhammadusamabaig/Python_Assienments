favorite_languages = {
 'jen': 'c#',
 'sarah': 'c',
 'edward': 'R',
 'phil': 'javascript',
 }
peopleList=['faraz','naeem','affan','adnan','jen','sarah','edward']
for i in peopleList:
    if i in favorite_languages:
        print(f'{i} thanks for responding')
    else:
        print(f'{i} please take poll')