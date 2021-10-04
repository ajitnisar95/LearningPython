import os,re;


path = "/home/ajit/Development/Python/File_Handling/pktdump/pktDumpP2"
pathofbasefile = "/home/ajit/Development/Python/File_Handling/pktdump"
counter = 0

print("path is %s" %path)
print("basepath is %s" %pathofbasefile)

os.chdir(pathofbasefile)
f = open("basefile3.txt", "w")
f.close()

def AppendToFile(data, pathofbasefile):
    os.chdir(pathofbasefile)
    #countcommas = 0
    #requireddata = ""
    #for element in data:
    #    if element == ',':
    #        countcommas+=1
    #        continue        
    #    if countcommas == 10:
    #        requireddata = requireddata+element
    #    elif countcommas == 11:
    #        requireddata = requireddata+','
    #    elif countcommas == 12:
    #        requireddata = requireddata+element
    #    elif countcommas == 13:
    #        break
    #newdata = "$EPB,QDNET,1.1.15,NR,L,869867031254545,7172,2,24092021,092738,18.979006,N,72.843643,E,0.2,189.26,15,5.10,1.01,0.65,Vodafone IN,0,1,25.3,4.1,10,31,404,20,7192,4CC4,404,20,7192,7B0E,-36,404,20,7192,4CC5,-54,404,20,7192,4CC3,-54,FB,2,69,39,-64,1,0,0,0,0,0,3.278,8991200010489039247F,996176,515A*"
    
    data = data.replace(",","",1)
    requireddata = ""
    count = 0
    for match in re.finditer(",(.*?),", data):
        count += 1
        if(count == 5 or count == 6):
            coord = match.group()
            coord = coord.replace(",","",2)
            requireddata = requireddata+coord
            if(count==5):
                requireddata = requireddata+","
        elif(count == 7):
            break
    print("\n"+requireddata)
        #print("match", count, match.group(), "start index", match.start(), "End index", match.end())

    f = open("basefile3.txt", "a")
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
        #if counter>1:
        #    break
    #else:
    #    continue