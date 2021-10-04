import sys
sys.setrecursionlimit(1000000000)
def infiniteloop(counter):
    #while(1):
    print("Infinite loop number %d" % counter)
    counter+=1
    infiniteloop(counter)
        


infiniteloop(1)