# Example of how to parse & extract data from a string

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21
sppos = data.find(' ',atpos) # starts the find at the @ sign
print(sppos) # 31
host = data[atpos+1 : sppos] # starts at character just after @ sign & goes to but not include the first space
print(host) # uct.ac.za
