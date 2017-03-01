import math
import random
import sys

class minheap:
    def __init__(self):
        self.heapindex={}
        self.heaparray=[]
        self.heapsize=-1
    def parent(self,i):
        if i==0: 
            return None
        else:
            return math.floor((i-1)/2)
    def left(self,i):
        if 2*(i+1)-1<=self.heapsize:
            return 2*(i+1)-1
        else: 
            return None
    def right(self,i):
        if 2*(i+1)<=self.heapsize:
            return 2*(i+1)
        else:
            return None
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l is not None:
            if l<=self.heapsize and self.heaparray[l][1]<self.heaparray[i][1]:
                smallest = l
            else:
                smallest = i
        else:
            smallest = i
        if r is not None:
            if r<=self.heapsize and self.heaparray[r][1]<self.heaparray[smallest][1]:
                    smallest = r
        if smallest!=i:
            self.heaparray[i], self.heaparray[smallest]=self.heaparray[smallest], self.heaparray[i]
            self.heapindex[self.heaparray[i][0]],self.heapindex[self.heaparray[smallest][0]]=self.heapindex[self.heaparray[smallest][0]],self.heapindex[self.heaparray[i][0]]
            self.heapify(smallest)
    def increasekey(self, i, value):
        p = self.parent(i)
        while i>0 and self.heaparray[p][1]>self.heaparray[i][1]:
            self.heaparray[i], self.heaparray[p]=self.heaparray[p], self.heaparray[i]
            self.heapindex[self.heaparray[i][0]],self.heapindex[self.heaparray[p][0]]=self.heapindex[self.heaparray[p][0]],self.heapindex[self.heaparray[i][0]]
            i = self.parent(i)
            p = self.parent(i)
    def insert(self,value):
        if self.heapindex:
            if value[0] in self.heapindex:
                id = self.heapindex[value[0]]
                if self.heaparray[id][1]>value[1]:
                    self.heaparray[id]=value
                    self.increasekey(id, value)
            else:
                self.heapsize += 1
                self.heaparray.append(value)
                self.heapindex[value[0]]=self.heapsize
                self.increasekey(self.heapsize, value)
        else:
            self.heapsize += 1
            self.heaparray.append(value)
            self.heapindex[value[0]]=self.heapsize
            self.increasekey(self.heapsize, value)
    def delete(self):
        min = self.heaparray[0]
        self.heaparray[0]=self.heaparray[self.heapsize]
        self.heapindex[self.heaparray[self.heapsize][0]]=0
        self.heaparray.pop()
        self.heapsize -= 1
        self.heapify(0)
        return min

def euclideanDist(a,b):
    temp = 0
    for i in range(len(a)):
        temp +=math.pow((a[i]-b[i]),2)
    return(math.sqrt(temp))

def genRandomGraph(n,d,t=0,nodes=None):
    edgedict={}
    threshold = cutOff(n,d,t)
    if d == 0:
        if nodes is None:
            nodes = range(n)
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    edge = [i,j,random.random()]
                    if edge[2]<threshold:
                        if i in edgedict:
                            edgedict[i].append(edge)
                        else:
                            edgedict[i] = edge
                        if j in edgedict:
                            edgedict[j].append(edge)
                        else:
                            edgedict[j] = edge
    else:
        if nodes is None:
            nodes = [[None]*d]*n
            nodes = [[random.random() for j in nodes[i]] for i in range(n)]
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    itup=tuple(nodes[i])
                    jtup=tuple(nodes[j])
                    edge = [itup,jtup,euclideanDist(nodes[i],nodes[j])]
                    if edge[2]<threshold:
                        if itup in edgedict:
                            edgedict[itup].append(edge)
                        else:
                            edgedict[itup] = [edge]
                        if jtup in edgedict:
                            edgedict[jtup].append(edge)
                        else:
                            edgedict[jtup] = [edge]
    return(nodes,edgedict)

def cutOff(n,d,extra=0):
    # multiply predicted cutoff by 2 to account for outliers
    if d ==0:
        return((3/math.pi)*(math.atan(-n/20)+math.pi/2)*2)
    elif d ==2:
        return((8/math.pi)*(math.atan(-n/20)+math.pi/2)+.01+extra)
    elif d==3:
        return((3/math.pi)*(math.atan(-n/30)+math.pi/2)+0.2+extra)
    elif d==4:
        return((3/math.pi)*(math.atan(-n/30)+math.pi/2)+2.0+extra)

def Prim(V,E,d):
    if d!=0:
        V = tuple(map(tuple, V))
    SP = set(V)
    distd = dict(zip(V,[math.inf]*len(V)))
    prevd = dict(zip(V,[None]*len(V)))
    distd[V[0]] = 0
    H = minheap()     
    H.insert((V[0],distd[V[0]]))
    while H.heapsize!=-1:
        v = H.delete() 
        if SP:
           SP.remove(v[0])
        for e in E[v[0]]:
            if v[0]==e[0]:
                w = e[1]
            else:
                w = e[0]
            if w in SP:
                if distd[w] > e[2]:
                    distd[w] = e[2]
                    prevd[w] = v[0]
                    H.insert((w,distd[w]))
    return (distd.values())
