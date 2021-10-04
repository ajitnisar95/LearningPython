import os;


path = "/home/ajit/Development/Python/File_Handling/pktdump/pktDumpP2"
pathofbasefile = "/home/ajit/Development/Python/File_Handling/pktdump"
counter = 0

print("path is %s" %path)
print("basepath is %s" %pathofbasefile)

os.chdir(pathofbasefile)
f = open("basefile2.txt", "w")
f.close()

def AppendToFile(data, pathofbasefile):
    os.chdir(pathofbasefile)
    countcommas = 0
    requireddata = ""
    for element in data:
        if element == ',':
            countcommas+=1
            continue        
        if countcommas == 10:
            requireddata = requireddata+element
        elif countcommas == 11:
            requireddata = requireddata+','
        elif countcommas == 12:
            requireddata = requireddata+element
        elif countcommas == 13:
            break
        

    f = open("basefile2.txt", "a")
    f.write(requireddata)
    f.write("\n\n")
    f.close()




for file in os.listdir(path):
    if file.endswith('.txt'):
        os.chdir(path)
        f = open(file, "r")
        data = f.read()
        f.close()
        AppendToFile(data, pathofbasefile)
        counter+=1
        print("Number of files successfully appended is %d" %counter)
        if counter>1000:
            break
    else:
        continue



