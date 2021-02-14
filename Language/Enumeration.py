###########################################################################################
###########################################################################################
# Working with Enumeration (and the second argument)

# This example and information was found in the article posted here:
# https://levelup.gitconnected.com/python-tricks-i-can-not-live-without-87ae6aff3af8

# This article delves deeper into enumeration which I plan to investigate further
###########################################################################################

mylist = ['a', 'b', 'd', 'c', 'g', 'e']
for i, item in enumerate(mylist):
    print(i, item)
# Will give:
0 a
1 b
2 d
3 c
4 g
5 e

# but, you can add a start for enumeration:
for i, item in enumerate(mylist, 16):
    print(i, item)
# and now you will get:
16 a
17 b
18 d
19 c
20 g
21 e

# It’s a simple start point of where enumeration should begin. 
# It can help you in situations where you are working on some kind of offsets logic.

###########################################################################################
###########################################################################################
