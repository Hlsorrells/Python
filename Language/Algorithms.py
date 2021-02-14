# Common algorithms

# Finding the largest value
myArray = [9,41,13,3,75,20]
maxNum = -1
for num in myArray :
    if num > maxNum :
        maxNum = num

# Finding the smallest value
smallest = None
for value in myArray :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value

# Counting in a Loop
count = 0
for thing in myArray :
    count += 1

# Summing in a Loop
count = 0
for thing in myArray :
    count = count + thing

# Finding Average in a Loop
count = 0
total = 0
for value in myArray :
    count += 1
    total = total + value
print('Average is', total / count)

# Filtering in a Loop
for value in myArray :
    if value > 20:
        return value

# Search using a Boolean variable
found = False
for value in myArray :
    if value == 9 :
        found = True
        break
