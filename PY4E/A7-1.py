# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Desired output:
# WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE
# AND REWARDING ACTIVITY  YOU CAN WRITE PROGRAMS FOR
# MANY REASONS RANGING FROM MAKING YOUR LIVING TO SOLVING
# A DIFFICULT DATA ANALYSIS PROBLEM TO HAVING FUN TO HELPING
# SOMEONE ELSE SOLVE A PROBLEM  THIS BOOK ASSUMES THAT
# {\EM EVERYONE} NEEDS TO KNOW HOW TO PROGRAM AND THAT ONCE
# YOU KNOW HOW TO PROGRAM, YOU WILL FIGURE OUT WHAT YOU WANT
# TO DO WITH YOUR NEWFOUND SKILLS

# WE ARE SURROUNDED IN OUR DAILY LIVES WITH COMPUTERS RANGING
# FROM LAPTOPS TO CELL PHONES  WE CAN THINK OF THESE COMPUTERS
# AS OUR PERSONAL ASSISTANTS WHO CAN TAKE CARE OF MANY THINGS
# ON OUR BEHALF  THE HARDWARE IN OUR CURRENT-DAY COMPUTERS
# IS ESSENTIALLY BUILT TO CONTINUOUSLY AS US THE QUESTION
# WHAT WOULD YOU LIKE ME TO DO NEXT

# OUR COMPUTERS ARE FAST AND HAVE VASTS AMOUNTS OF MEMORY AND
# COULD BE VERY HELPFUL TO US IF WE ONLY KNEW THE LANGUAGE TO
# SPEAK TO EXPLAIN TO THE COMPUTER WHAT WE WOULD LIKE IT TO
# DO NEXT IF WE KNEW THIS LANGUAGE WE COULD TELL THE
# COMPUTER TO DO TASKS ON OUR BEHALF THAT WERE REPTITIVE
# INTERESTINGLY, THE KINDS OF THINGS COMPUTERS CAN DO BEST
# ARE OFTEN THE KINDS OF THINGS THAT WE HUMANS FIND BORING
# AND MIND-NUMBING

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
words = fh.read()
print(words.upper())