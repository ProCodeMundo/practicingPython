
# Variables: are used to store values.  
# String: is a series of characters surrounded by single or double quotes

# Print statement
print("Hi")

# Print Statement with a variable
msg = "Hello world"
print(msg)

# Concatanation: combining string
first_name = 'Jhon'
last_name  = 'Doe'
full_name = first_name + ' '+ last_name
print(full_name)

# List: as lists store a series of times in a particualr order, you acces items using an index or within a loop
listItems = ['cup', 'tree', 'house']
print(listItems)
# Get the first item 
firstItem = listItems[0]
print(firstItem)
# Get the last item
lastItem = listItems[-1]
print(lastItem)
# Looping throug a list
for x in listItems:
    print(x)
# Adding items to a list 
listItems.append('car')
listItems.append('tablet')
listItems.append('plane')
print(listItems)
# Printing index of Fifth Item. 
listItem = listItems[5]
print(listItem)

# Making numerical list
square = []
for x in range (1, 11):
    square.append(x**2)
    print(x)
    print(square)

# Slicing a list
first_two = listItems[:2]
print(first_two)

# copy a list 
copy_of_items = listItems[:]
print(copy_of_items)




