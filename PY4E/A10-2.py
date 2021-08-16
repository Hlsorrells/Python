# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Desired Output
    # 04 3
    # 06 1
    # 07 1
    # 09 2
    # 10 3
    # 11 6
    # 14 1
    # 15 2
    # 16 4
    # 17 2
    # 18 1
    # 19 1

# Get file name from user
name = input('Enter file: ')
# Make sure file name is not blank
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name)

# Declare global variables
counts = dict()

# Loop over the lines in the handle
for line in handle:
    line = line.rstrip()
    #  Find lines that start with "From:" to identify senders
    if line.startswith('From ') :
        # Split the line into a list of individual words
        words = line.split()
        # Assign the fifth word as list of time elements
        time = words[5].split(':')
        # Pull out the hour element
        hour = time[0]
        # Count the number of times the hour is listed in the file
        counts[hour] = counts.get(hour,0) + 1

# Print the sorted dictionary items by (hour, count)
for k, v in sorted(counts.items()):
    print(k,v)
