# Opening a file & handling a bad file name

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:')
        count += 1
print('There were',count,'subject lines in',fname)

