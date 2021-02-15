# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines 
# as the person who sent the mail. The program creates a Python dictionary that 
# maps the sender's mail address to a count of the number of times they appear 
# in the file. After the dictionary is produced, the program reads through the 
# dictionary using a maximum loop to find the most prolific committer.
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# Get file name from user
name = input('Enter file: ')
# Make sure file name is not blank
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name)

# Global variables declared
counts = dict()
maxCount = -1
maxEmail = dict()

# Loop over the lines in the handle
for line in handle:
    line = line.rstrip()
    #  Find lines that start with "From:" to identify senders
    if line.startswith('From:') :
        # Split the line into a list of individual words
        words = line.split()
        # Assign the second word as the email address
        email = words[1]
        # Count the number of times the email is listed in the file
        counts[email] = counts.get(email,0) + 1

# Loop over the dictionary of emails and counts that are pulled from the file
for email, count in counts.items():
    # Convert the count to an integer for comparison operator
    num = int(count)
    # compare the current count to the maxCount
    if num > maxCount :
        # Set the new maximum count
        maxCount = num
        # Empty the current maxEmail object
        maxEmail = {}
        # Set the new email object with the maximum count
        maxEmail[email] = count

# Print the new dictionary as a single key value pair without the notation
for email, count in maxEmail.items():
    print(email, count)

