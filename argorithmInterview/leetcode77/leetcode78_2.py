class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans =[]
        def dfs(start,k,array):
            if k == 0 :
                ans.append(array[:])
            else:
                for i in range(start,n+1):
                    array.append(i)
                    dfs(i+1,k-1,array)
                    array.pop(-1)
        dfs(1,k,[])
        return ans
