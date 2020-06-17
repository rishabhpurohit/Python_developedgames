fname = input("Enter file name: ")
fh = open(fname)
data=[]
for each in fh:
    words=each.split()
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))


#data
#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief
