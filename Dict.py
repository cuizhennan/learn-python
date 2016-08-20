bob = {'name':'Bob Smith','age':42,'pay':3000,'position':'software'}
sue = {'name':'Sue Jones','age':45,'pay':4000,'position':'hardware'}

print(bob['name'],',',sue['name'])
print(bob['name'].split()[-1])

sue['pay'] *= 1.10
print(sue['pay'])

bobs = dict(name='Bob Smith',age=42)
sues = dict(name='Sue Jones',age=45)
print(bobs,sues)

bobs['pay'] = 3000
bobs['position'] = 'software'
sues['pay'] = 4000
sues['position'] = 'hardware'
print(bobs,sues)

# dict list
print('----- dict list -------')
people = [bobs,sues]
for person in people:
    print(person['name'],person['pay'],sep=',')
    if person['name'] == 'Bob Smith':
        print(person['pay'])

# zip()
print('-------use zip() ---------')
names = ['name','age','pay','position']
values =['Bob Smith',43,3000,'software']
print(list(zip(names,values)))
suenew = dict(zip(names,values))
print(suenew)

# init dict()
print('-------init dict() ---------')
fields = ('name','age','job','pay')
record = dict.fromkeys(fields,'?')
print(record)

# collect names
print('------collect names ----------')
namenews = [person['name'] for person in people]
print(namenews)

# map()
print('------use map() --------')
resultmaps = list(map((lambda x:x['name']),people))
print(resultmaps)

# sum()
print('------ use sum() --------')
resultsums = sum(person['pay'] for person in people)
print(resultsums)

# next()
print('------ use next() --------')
G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

# dict is dict
print('------dict is dict--------')
db={}
db['bob'] = bob
db['sue'] = sue
import pprint
pprint.pprint(db)

print(list(db['bob'].values()))
