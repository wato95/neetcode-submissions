class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(perm, nums, pick):
            if len(perm) == len(nums):
                res.add(tuple(perm.copy()))
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, nums, pick)
                    perm.pop()
                    pick[i] = False

        
        backtrack([], nums, [False] * len(nums))
        return list(res)