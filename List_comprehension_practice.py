# new_list = [expression for item in iterable if condition]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [fruit for fruit in fruits if fruit]
print(newlist) 

list = []
for item in fruits:
    list.append(item)
print(list)

# Find all of the numbers from 1-1000 that are divisible by 7

divbyseven = [ num for num in range(1000) if num % 7 == 0]
print(divbyseven)

# Find all of the numbers from 1-1000 that have a 3 in them

numbers = [num for num in range(0,1000) if '3' in str(num)]
print(numbers)

# Count the number of spaces in a string

string = 'the slow solid squid swam sumptuously through the slimy swamp'

spaces = [ i for i in string if i == ' ']
print(len(spaces))

# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday 
# they yodled while eating yuky yams”

string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

consonants = [ char for char in string if char not in 'a, e, i, o, u']
print(consonants)

# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common = [ num for num in list_a if num in list_b]
print(common)

# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest 
# with over 1000 people attending’

stringone = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

nums = [ k for k in stringone if k.isdigit() ] 
print(nums)

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, 
# and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

numbers = range(20)
result = [ 'even' if b % 2 == 0 else 'odd' for b in numbers ]
print(result)

# Produce a list of tuples consisting of only the matching numbers in these lists 
# list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

lista = [1, 2, 3,4,5,6,7,8,9]
listb = [2, 7, 1, 12]

pares = [(i, j) for i in lista for j in listb if i == j ]
print(pares)
