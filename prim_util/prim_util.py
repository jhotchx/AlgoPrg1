import itertools as it
import time as time
import math
import numpy as np

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

def genRandomGraph(nodes,dimension):
   # first graph type
   if dimension==0:
       nodes = range(nodes)
       edges = [(x,np.random.rand()) for x in it.combinations(nodes,2)]
   # multidimensional graphs
   else:
       nodes = np.random.rand(nodes,dimension)
       edges = [((p0,p1),np.linalg.norm(p0-p1)) for p0,p1 in it.combinations(nodes,2)]
   return (nodes,edges)

def cutOff(n,d,extra=0):
    # multiply predicted cutoff by 2 to account for outliers
    if d ==0:
        return(math.exp(.0631-.066*n+.000721*math.pow(n,2)-.000003087*math.pow(n,3))+extra)
    elif d ==2:
        return((8/np.pi)*(np.arctan(-n/20)+np.pi/2)+.01+extra)
    else:
        return()

def Prim(V,E,d,t=0,x=0):
    threshold = cutOff(len(V),d,x)
    E = [edge for edge in E if edge[1]<threshold]
    if d!=0:
        V = tuple(map(tuple, V))
    SP = set(V)
    #print("Initial SP=",SP)
    distd = dict(zip(V,[math.inf]*len(V)))
    prevd = dict(zip(V,[None]*len(V)))
    distd[V[0]] = 0
    H = minheap()     #Heap
    H.insert((V[0],distd[V[0]]))
    while H.heapsize!=-1:
        v = H.delete() 
        if SP:
           SP.remove(v[0])
        for e in E:
            if d!=0:
                enodes = [tuple(i) for i in e[0]]
            else:
                enodes = e[0]
            if v[0] in enodes:
                w = enodes[1-enodes.index(v[0])]
                if w in SP:
                    if distd[w] > e[1]:
                        distd[w] = e[1]
                        prevd[w] = v[0]
                        H.insert((w,distd[w]))
    if not any(dist ==math.inf for dist in distd.values()):
        return (sum(distd.values()))
    else:
        print(t)
        t+=1
        return(Prim(V,E,d,.01*t))