class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        i = 0
        for val in nums:
            ans[i] = val
            ans[n + i] = val
            i += 1
        return ans
