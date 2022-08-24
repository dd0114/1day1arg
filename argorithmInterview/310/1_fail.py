class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        hh = 10**5
        dist = collections.defaultdict(list)
        
        link = [[] for _ in range(n)]
        
        for l,r in edges:
            link[l].append(r)
            link[r].append(l)
        
        visit = [False] * n
        
        q = collections.deque([])
        q.append((None,0))
        
        while q:
            p,node = q.popleft()
            visit[node] = True
            
            for i in link[node]:
                if i == p:
                    continue
                q.append((node,i))
                dist[node].append((1,i))
                dist[i].append((1,node))
            
            for i in link[node]:
                for d,n in dist[node]:
                    if n == i:
                        continue
                    dist[i].append((d+1,n))
                    dist[n].append((d+1,n))
            
        ans = hh
        print(dist)
        for i in dist:
            tmp = 0
            for j in dist[i]:
                tmp = max(tmp,j[1])
            ans = min(tmp,ans)
            
        return ans