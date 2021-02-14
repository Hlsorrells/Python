# Find the unique elements by using set 
# A set is an unordered collection with no duplicate elements (Case sensitive!).

myword = "NanananaBatman"
set(myword)
{'N', 'm', 'n', 'B', 'a', 't'}

# first you can easily change set to list and other way around
mylist = ["a", "b", "c", "c"]
# let's make a set out of it
myset = set(mylist)
# myset will be:
{'a', 'b', 'c'}
# and, it's already iterable so you can do:
for element in myset:
    print(element)
# but you can also convert it to list again:
mynewlist = list(myset)
# and mynewlist will be:
['a', 'b', 'c']

mylist = ["c", "c", "a", "b"]
mynewlist = list(set(mylist))
# mynewlist is:
['a', 'b', 'c']
# as you can see it's different order;