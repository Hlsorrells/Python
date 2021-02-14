# Conditional Statements

#If statements & Conditional Operators
if x == 5:
    print('Equals operator')
if x < 10:
    print('Less than operator')
if x <= 10:
    print('Less than or Equal to operator')
if x > 10:
    print('Greater than operator')
if x >= 10:
    print('Greater than or Equal to operator')
if x != 10:
    print('Not Equal operator')
print('Finished')


# If / Else statements
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x > 20:
    print('Large')
else:
    print('Biggest')
print('Finished')


# Try / Except statement
aStr = 'Bob'
try:
    print('Hello')
    istr = int(aStr)
    print('There')
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('This is a number')
else:
    print('Not a number')
