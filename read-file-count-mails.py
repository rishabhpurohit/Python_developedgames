name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

dict1 = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    dict1[words[1]] = dict1.get(words[1],0)+1

largest = None
largest_author = None

for key in dict1:
    if largest is None: largest = dict1[key]

    if largest < dict1[key]:
        largest = dict1[key]
        largest_author = key

print(largest_author, largest)
#
#
#
#
#
###v

###
#
#
v##
#
#
#
#
v#
v
#

#
vv

v#
##
#
v
vv##
v
v
#
v
##v
#
#
#
vv
v
#
##
v
#
