# Loop statements


# While statement
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

while True:
    line = input('> ')
    if line[0] == "#" :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# For statement
for i in [5,4,3,2,1] :
    print(i)
print('Done')

friends = ['Jo', 'Star', 'Devon']
for friend in friends :
    print('Happy New Year:', friend)
print('Done')
