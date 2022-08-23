class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans =[]
        def dfs(array):
            nonlocal k
            nonlocal n
            nonlocal ans
            
            if array == []:
                for i in range(1,n+1):
                    tmp = array[:]
                    tmp.append(i)
                    if len(tmp) == k:
                        ans.append(tmp)
                    else:
                        dfs(tmp)
            else:
                for i in range(array[-1]+1,n+1):
                    tmp = array[:]
                    tmp.append(i)
                    if len(tmp) == k:
                        ans.append(tmp)
                    else:
                        dfs(tmp)
        
        if k == 0:
            return []
        
        dfs([])

        return ans
        