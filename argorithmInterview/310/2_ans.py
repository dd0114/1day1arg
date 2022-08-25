class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ind = [0]*n
        link = [[] for _ in range(n)]
        if n == 1:
            return([0])
        
        for l,r in edges:
            ind[l] +=1
            ind[r] +=1
            link[l].append(r)
            link[r].append(l)
        
        q = []
        
        for i in range(n):
            if ind[i] == 1:
                q.append(i)
        
        
        while n>2:
            n -= len(q)
            new = []
            for node in q:
                nei = link[node].pop()
                link[nei].remove(node)
                
                if len(link[nei]) == 1:
                    new.append(nei)
            
            q= new[:]
        
        
        return q
        