class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and nums[i-1] == num:
                continue
                
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tot = num + nums[l] + nums[r]

                if tot == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
            
        return ans
