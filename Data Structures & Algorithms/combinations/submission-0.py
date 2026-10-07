class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]

        
        def dfs(i, sub_array):
            if len(sub_array) == k:
                res.append(sub_array.copy())
                return
                
            if i >= n:
                return
            sub_array.append(nums[i])
            dfs(i+1, sub_array)
            sub_array.pop()
            dfs(i+1, sub_array)

        dfs(0, [])
        return res
