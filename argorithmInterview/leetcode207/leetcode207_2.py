#dfs로 순환되는 경우의 수를 찾기

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c_dict = collections.defaultdict(list)
        
        for i,j in prerequisites:
            c_dict[i].append(j)
        
        traced = set()
        visited = set()
        
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)
            for j in c_dict[i]:
                if not dfs(j):
                    return False 

            traced.remove(i)
            visited.add(i)    
            return True

        for x in list(c_dict):
            if not dfs(x):
                return False

        return True