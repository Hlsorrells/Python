# The := operator is officially known as the assignment expression operator. During early discussions, it was dubbed the walrus operator because the := syntax resembles the eyes and tusks of a sideways walrus. You may also see the := operator referred to as the colon equals operator. Yet another term used for assignment expressions is named expressions.

# Use Cases 
# Repeated function calls can make your code slower than necessary.
# Repeated statements can make your code hard to maintain.
# Repeated calls that exhaust iterators can make your code overly complex.

# Assignment statement -- does not return a value (have to call the variable)
>>> walrus = False
>>> walrus
False

# Assignment expression -- returns the value of the variable
>>> (walrus := True)
True
>>> walrus
True