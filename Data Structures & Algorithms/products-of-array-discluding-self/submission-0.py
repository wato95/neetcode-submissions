class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        i = 0
        while i < n:
            if i == 0:
                prefix[i] = 1
                previous = 1
            else:
                new = previous * nums[i-1]
                prefix[i] = new
                previous = new
            i += 1

        j = n-1
        while j >= 0:
            if j == n-1:
                suffix[j] = 1
                previous = 1
            else:
                new = previous * nums[j+1]
                suffix[j] = new
                previous = new
            j -= 1
        
        result = [prefix[i] * suffix[i] for i in range(n)]
        
        return result
        