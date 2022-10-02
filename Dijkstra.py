# Problem website: https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

'''
Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that  edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.
'''

import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        visit = set()               
        dist = [float('inf')] * V
        dist[S] = 0
        heap = [(0, S)]
        heapq.heapify(heap)
        while heap:
            w, d = heapq.heappop(heap)
            if d in visit:
                continue
            visit.add(d)
            for j, k in adj[d]:
                dist[j] = min(dist[j], dist[d]+k)
                heapq.heappush(heap, (dist[j],j))
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends