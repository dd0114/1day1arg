class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(cnt,array):           
            ans.append(array)
            for i in range(cnt,len(nums)):
                dfs(i+1,array+[nums[i]])
            
        dfs(0,[])
        
        return ans