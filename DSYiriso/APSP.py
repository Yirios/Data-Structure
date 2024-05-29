'''
The All Pairs Shortest Path (APSP) calculates 
the shortest (weighted) path between all pairs of nodes.
https://neo4j.com/docs/graph-data-science/current/algorithms/all-pairs-shortest-path/
'''

from priorityQueue import PriorityQueue
from Graph import Graph
import sys


def dijkstra(G,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        nowVert = pq.delMin()
        for nextVert in nowVert.getConnections():
            newDist = nowVert.getWeight(nextVert) + nowVert.getDistance()
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(nowVert)
                pq.decreaseKey(nextVert,newDist)

def getAllPairsShortestPath(G,keys):
    result = [['#' for _ in range(len(keys))]for _ in range(len(keys))]
    for key in keys:
        dijkstra(G,G.getVertex(key))
        for v in G:
            if v.getDistance() not in (0,sys.maxsize):
                G.addEdge(key,v.getId(),v.getDistance())
            v.setDistance(sys.maxsize)
    
    for i,key in enumerate(keys):
        Vertfrom = G.getVertex(key)
        for neighbor in Vertfrom.getConnections():
            j = keys.find(neighbor.getId())
            result[i][j] = str(Vertfrom.getWeight(neighbor))
    
    return result
