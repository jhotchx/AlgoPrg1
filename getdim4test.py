import prim_util.prim_util_space as pu
import importlib as imp
import math
import statistics
import time
imp.reload(pu)

#@profile
def randmst(n,trials,d):
    treelen = []
    maxnodes = []
    for i in range(trials):
        nodes,edges = pu.genRandomGraph(n,d)
        res = pu.Prim(nodes,edges,d)
        t = 0
        while any(dist ==math.inf for dist in res):
            t+=.01
            nodes,edges = pu.genRandomGraph(n,d,t,nodes,edges)
            res = pu.Prim(nodes,edges,d)
        treelen.append(sum(res))
        maxnodes = [max(res)]
    print('the average minimum spanning tree weight for a graph with',len(nodes),'nodes in',dimension,'dimensions, over',trials,'trials was:',statistics.mean(treelen))
    return(treelen, maxnodes)

if __name__ == "__main__":
    dimension=4
    values = []
    tree = []
    for nodenum in range(2,101):
        a=time.perf_counter()
        t,m = randmst(nodenum,50,dimension)
        values.append(m)
        b=time.perf_counter()
        print(nodenum,b-a)    
    for nodenum in range(110,210,10):
        a=time.perf_counter()
        t,m = randmst(nodenum,20,dimension)
        values.append(m)
        b=time.perf_counter()
        print(nodenum,b-a)
    for nodenum in range(225,425,25):
        a=time.perf_counter()
        t,m = randmst(nodenum,10,dimension)
        values.append(m)
        b=time.perf_counter()
        print(nodenum,b-a)
    for nodenum in range(450,850,50):
        a=time.perf_counter()
        t,m = randmst(nodenum,10,dimension)
        values.append(m)
        b=time.perf_counter()
        print(nodenum,b-a)
    for nodenum in range(850,1550,100):
        a=time.perf_counter()
        t,m = randmst(nodenum,10,dimension)
        values.append(m)
        b=time.perf_counter()
        print(nodenum,b-a)
        