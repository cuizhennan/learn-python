bob = [['name','Bob Smith'],['age',42],['pay',3000],['position','software']]
sue = [['name','Sue Jones'],['age',45],['pay',4000],['position','hardware']]
people =[bob,sue]

# for person in people:
#     print(person[0][1],person[2][1])

# for person in people:
#     for (name,value) in person:
#         print(name,value)
#         if name == 'name':
#             print(value)

def field(record,label):
    for (fname,fvalue) in record:
        if fname == label:
            return fvalue

resVal = field(bob,'name')
print(resVal)

for rec in people:
    print(field(rec,'age'))