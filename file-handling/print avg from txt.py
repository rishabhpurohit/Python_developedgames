# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
y=average=count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    y=float(line[21:27])
    average=average+y
    count=count+1
avg = average/count
print("Average spam confidence: " + str(avg))
