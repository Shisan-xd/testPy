dict1 = {'name': 'Tom', 'age': 18, 'gender': '男'}

for iu in dict1.values():
    print(iu)

for iu in dict1.keys():
    print(iu)


for iu in dict1.items():
    print(iu)


for iu, io in dict1.items():
    print(f'{iu} : {io}')

