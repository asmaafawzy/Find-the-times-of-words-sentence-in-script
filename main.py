# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:54:19 2018

@author: Asmaa
"""

keys = []
values = [] 
lines = []

f = open("data.txt", 'r')
lines = f.readlines()
x = len(lines)
#print(lines)
f.close()
i = 0
j = 1
times = []
for line in range(0, len(lines),2):
    keys.append(lines[line])
for line in range(1, len(lines),2):
    values.append(lines[line].lower()) # values to search with lowercase only in the file.

print("Enter the word/sentence")
x = input()
c = -1
f = 0                        #flag to check valid inputs 
wri = open('times.txt', 'a') # file to save the times founded in the search results.
for word in values:
    c += 1
    if x in word:   
        print(word)
        index = word.index(x)
        time = keys[c]
        wri.write(time)
        print(time)

wri.close()      


    







