from prim_util.prim_util_space import *
import statistics
import sys

testing = sys.argv[1]
nodes = int(sys.argv[2])
trials = int(sys.argv[3])
dimension = int(sys.argv[4])

#@profile
def main(n,trials,d):
    results = []
    for i in range(trials):
        nodes,edges = genRandomGraph(n,d)
        res = Prim(nodes,edges,d)
        t = 0
        while any(dist ==math.inf for dist in res):
            t+=.01
            nodes,edges = genRandomGraph(n,d,t,nodes,edges)
            res = Prim(nodes,edges,d)
        else: 
            results.append(sum(res))
    print('the average minimum spanning tree weight for a graph with',len(nodes),'nodes in',dimension,'dimensions, over',trials,'trials was:',statistics.mean(results))

if __name__ == "__main__":
    main(nodes,trials,dimension)
