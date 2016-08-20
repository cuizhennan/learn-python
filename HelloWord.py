bob = ['Bob Smith',42,3000,'software']
sue = ['Sue Jones',45,4000,'hardware']

people  = [bob,sue]
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

for person in people:
    print(person[2])

pays =[person[2] for person in people]
print(pays)

# map()
pays = map((lambda x:x[2]),people)
print(list(pays))

# sum()
total = sum(person[2] for person in people)
print(total)

print(len(people))

# append()
people.append(['Tom',50,0,None])

# len()
print(len(people))
print(people)

NAME,AGE,PAY = range(3)
print(bob[NAME])
print(bob[AGE])
print(bob[PAY])

for person in people:
    print(person[NAME])