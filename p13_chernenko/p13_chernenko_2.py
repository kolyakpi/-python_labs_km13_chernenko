import os

#В мене з цим шляхом працювало...
#directory = os.fsencode('/home/kolya/Desktop/Studying/pythonHomeworks/p12_chernenko/archive')
#З цим не впевнений бо не первіряв
directory = os.fsencode('/archive')
filenames = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        #В мене з цим шляхом працювало...
        #filenames.append(('/home/kolya/Desktop/Studying/pythonHomeworks/p12_chernenko/archive/{0}'.format(filename)))
        #З цим не впевнений бо не первіряв
        filenames.append(('/archive/{0}'.format(filename)))
        
man_global_name=["Michael"]
man_global_count=[1]
woman_global_name=["Lisa"]
woman_global_count=[1]

count = 1
for file in filenames:
    print(count)
    count+=1
    f = open(file, 'r')
    
    woman_local_name = ""
    line1 = f.readline()
    stringw=''
    for i in line1:
        if i != ",":
            stringw += i
        else:
            break
    woman_local_name = stringw
    
    man_local_name = ""
    
    for line in f:
            
        if ",M," in line:
            string = ""
            counter = 0
            for i in line:
                if i != ",":
                    string += i
                else:
                    if counter == 0:
                        man_local_name = string
                        counter += 1
                        string = "" 
            break        
        
    print("man:", man_local_name)
    print("woman: ", woman_local_name)

    if man_local_name in man_global_name:
        ind = man_global_name.index(man_local_name)
        man_global_count[ind] += 1
    else:
        man_global_name.append(man_local_name)
        man_global_count.append(1)
        
    if woman_local_name in woman_global_name:
        ind = woman_global_name.index(woman_local_name)
        woman_global_count[ind] += 1
    else:
        woman_global_name.append(woman_local_name)
        woman_global_count.append(1)

mistake = 1
while mistake ==1:
    mistake = 0
    for i in range(len(man_global_count)):
        if i != len(man_global_count) - 1:
            if man_global_count[i] > man_global_count[i+1]:
                num = man_global_count[i]
                man_global_count[i] = man_global_count[i+1]
                man_global_count[i+1] = num
        
                name = man_global_name[i]
                man_global_name[i] = man_global_name[i+1]
                man_global_name[i+1] = name
                mistake = 1

mistake = 1   
while mistake == 1:
    mistake = 0
    for i in range(len(woman_global_count)):
        if i != len(woman_global_count) - 1:
            if woman_global_count[i] > woman_global_count[i+1]:
                num = woman_global_count[i]
                woman_global_count[i] = woman_global_count[i+1]
                woman_global_count[i+1] = num
        
                name = woman_global_name[i]
                woman_global_name[i] = woman_global_name[i+1]
                woman_global_name[i+1] = name
                mistake = 1
            

            
for i in reversed(range(len(man_global_count))):
    print(man_global_name[i] , ": ", man_global_count[i])
print("")    
for i in reversed(range(len(woman_global_count))):
    print(woman_global_name[i] , ": ", woman_global_count[i])




