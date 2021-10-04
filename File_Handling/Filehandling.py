import os;


path = "/home/ajit/Development/Python/File_Handling/pktdump/pktDumpP2"
pathofbasefile = "/home/ajit/Development/Python/File_Handling/pktdump"
counter = 0

print("path is %s" %path)
print("basepath is %s" %pathofbasefile)

os.chdir(pathofbasefile)
f = open("basefile.txt", "w")
f.close()

def AppendToFile(data, pathofbasefile):
    os.chdir(pathofbasefile)
    datarequired = data[62:85]
    datarequired =datarequired.replace(",N","")
    datarequired =datarequired.replace(",E","")
    f = open("basefile.txt", "a")
    f.write(datarequired)
    f.write("\n\n")
    f.close()

def Readfile(filename):
    pass


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



