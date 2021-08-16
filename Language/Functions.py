# Functions

# Functions are first-class citizens in Python:
    # They can be passed as arguments to other functions,
    # returned as values from other functions, and
    # assigned to variables and stored in data structures.

# Define a function
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), "Manual")

def addtwo (a,b):
    added = a + b
    return added


# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
