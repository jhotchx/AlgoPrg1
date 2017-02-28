from prim_util.prim_util import *
import sys

testing = sys.argv[1]
nodes = int(sys.argv[2])
trials = int(sys.argv[3])
dimension = int(sys.argv[4])

@profile
def main(nodes,trials,dimension):
    nodes,edges = genRandomGraph(nodes,dimension)
    for i in range(trials):
        t=0
        Prim(nodes,edges,dimension)

if __name__ == "__main__":
    main(nodes,trials,dimension)