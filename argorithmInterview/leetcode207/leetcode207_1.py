class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        link = [[] for _ in range(numCourses)]
        ind = [0]*numCourses
        for i,j in prerequisites:
            ind[i] += 1
            link[j].append(i)
        
        q = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        
        cnt = numCourses
        pointer = 0
        while pointer < len(q):
            cnt -=1
            tmp = q[pointer]
            for i in link[tmp]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
            pointer +=1
                
        if cnt == 0:
            return True
        else:
            return False