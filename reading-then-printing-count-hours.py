name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hourcount= dict()
one =[]                                        
for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':      
        hr = words[5].split(':')                   
        hourcount[hr[0]] = hourcount.get(hr[0], 0) + 1   
for k,v in hourcount.items():                          
    one.append((k,v))             
one.sort()                                        
for k,v in one:                                    
    print (k,v)         
