greeting ='Hello, World!'
#index = 0

"""for letter in enumerate(greeting):
   print(f'Index: {index}, Letter: {greeting[index]}')
  index += 1"""
"""
for index,item in enumerate(greeting):
    print(f'Index: {index}, Letter: {item}')
"""

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list(zip(list1, list2))) #elemanları sırayla eşleştirir ve bir liste oluşturur.

for item1, item2 in zip(list1, list2):
    print(f'Item1: {item1}, Item2: {item2}')



