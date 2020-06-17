fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
li=[]
for i in fh:
    # To check whether the line have more than two elements space seperated
    if i.startswith("From") and len(i.split())>2:
        temporary=i.split()
        li.append(temporary[1])
for i in li:
    print(i)
print("There were", len(li), "lines in the file with From as the first word")
