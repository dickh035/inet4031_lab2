#!/usr/bin/env python3

fileobj = open("fileprocessor.input", "r")

data = fileobj.read()

lis = data.split('\n')

def makelist(lis):
 result = []
 for elem in lis:
  sub = elem.split(', ')
  result.append(sub)

 return(result)

newlist = []
for el in lis:
 s = el.split(':')
 newlist.append(s)

print("Printing out User Data")
print(" ")

for x in range(3):
 print("The user " + newlist[x][0] + " has a password of " + newlist[x][1] + " and has userid " + newlist[x][2] + " and groupid " + newlist[x][3] )

print("User4 os skipped because it starts with a hashtag (is commented out)")
print(" ")
print("End of User Data")
fileobj.close()
