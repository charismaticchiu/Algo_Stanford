data = open("SCC.txt","r")
G = {}
for i in range(1,875715):
    G[i] = []
#print G[1]   
fst = 1
empt = []
for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]].append(lst[1])
    #print G[lst[0]]

print G[1]

