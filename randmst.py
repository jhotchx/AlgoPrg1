from prim_util.prim_util import *
import sys

testing = sys.argv[1]
nodes = int(sys.argv[2])
trials = int(sys.argv[3])
dimension = int(sys.argv[4])

#@profile
def main(nodes,trials,dimension):
    nodes,edges = genRandomGraph(nodes,dimension)
    results = []
    for i in range(trials):
        results.append(Prim(nodes,edges,dimension))
    print('the average minimum spanning tree weight for a graph with',len(nodes),'nodes in',dimension,'dimensions, over',trials,'trials was:',np.mean(results))

if __name__ == "__main__":
    main(nodes,trials,dimension)