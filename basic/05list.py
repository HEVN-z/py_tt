import random

list1 = [10,5,3,7,9,2,1,4,6,8,7,3]
print('print list1\t\t\t',list1)
print('count 7 in list\t\t\t',list1.count(7)) # Count number of 7 in list
print('get index of 8 in list\t\t',list1.index(8)) # Get index of 8 in list
list1.append(11) # Add 11 to list
print('append 11 to list\t\t',list1)
list1.insert(0,2) # Insert 2 to index 0
print('insert 2 to index 0\t\t',list1)
list1.remove(11) # Remove 11 from list
print('remove 11 from list\t\t',list1)
list1.pop() # Remove last element from list
print('pop last element from list\t',list1)
list1.pop(0) # Remove element at index 0
print('pop element at index 0\t\t',list1)


list1.sort() # Sort list
print('sort list\t\t\t',list1)

random.shuffle(list1) # Shuffle list
shuf1 = list1.copy() # Copy list
print('shuffle list\t\t\t',list1)
print('shuf1 copy from list1\t\t',shuf1)

random.shuffle(list1) # Shuffle list again
shuf2 = list1.copy() # Copy list
print('shuffle list again\t\t',list1)
print('shuf2 copy from list1\t\t',shuf2)

shuf3 = shuf1 + shuf2 # Add two list
print('shuf3 = shuf1 + shuf2\t\t',shuf3)

shuf3 = shuf2 + shuf1 # Add two list
print('shuf3 = shuf2 + shuf1\t\t',shuf3)

shuf4 = shuf1 * 2 # Multiply list by 2 Number is not multiple but add list to itself as multiply
print('shuf4 = shuf1 * 2\t\t',shuf4)

# shuf4 = shuf1 - shuf2 # Subtract two list
# print('shuf4 = shuf1 - shuf2\t\t',shuf4)
## Err = TypeError: unsupported operand type(s) for -: 'list' and 'list'