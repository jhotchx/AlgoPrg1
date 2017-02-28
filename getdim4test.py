import prim_util.prim_util_space as pu
import importlib as imp
import statistics as stat
import time
imp.reload(pu)

def main():
    d=4
    values = []
    tree = []
    for nodenum in range(2,101):
       a=time.perf_counter()
       tempVal = []
       tempTree = []
       for trials in range(100):
           nodes,edges = pu.genRandomGraph(nodenum,d)
           x= pu.Prim(nodes,edges,d)
           tempVal.append(max(x.values()))
           tempTree.append(sum(x.values()))
       values.append(max(tempVal))
       tree.append(stat.mean(tempTree))
       b=time.perf_counter()
       print(nodenum,b-a)    
    for nodenum in range(110,210,10):
       a=time.perf_counter()
       tempVal = []
       tempTree = []
       for trials in range(20):
           nodes,edges = pu.genRandomGraph(nodenum,d)
           x= pu.Prim(nodes,edges,d)
           tempVal.append(max(x.values()))
           tempTree.append(sum(x.values()))
       values.append(max(tempVal))
       tree.append(stat.mean(tempTree))
       b=time.perf_counter()
       print(nodenum,b-a) 
    for nodenum in range(225,425,25):
       a=time.perf_counter()
       tempVal = []
       tempTree = []
       for trials in range(10):
           nodes,edges = pu.genRandomGraph(nodenum,d)
           x= pu.Prim(nodes,edges,d)
           tempVal.append(max(x.values()))
           tempTree.append(sum(x.values()))
       values.append(max(tempVal))
       tree.append(stat.mean(tempTree))
       b=time.perf_counter()
       print(nodenum,b-a) 
    for nodenum in range(450,850,50):
       a=time.perf_counter()
       tempVal = []
       tempTree = []
       for trials in range(10):
           nodes,edges = pu.genRandomGraph(nodenum,d)
           x= pu.Prim(nodes,edges,d)
           tempVal.append(max(x.values()))
           tempTree.append(sum(x.values()))
       values.append(max(tempVal))
       tree.append(stat.mean(tempTree))
       b=time.perf_counter()
       print(nodenum,b-a) 
    for nodenum in range(850,1550,100):
       a=time.perf_counter()
       tempVal = []
       tempTree = []
       for trials in range(10):
           nodes,edges = pu.genRandomGraph(nodenum,d)
           x= pu.Prim(nodes,edges,d)
           tempVal.append(max(x.values()))
           tempTree.append(sum(x.values()))
       values.append(max(tempVal))
       tree.append(stat.mean(tempTree))
       b=time.perf_counter()
       print(nodenum,b-a)
       
main()