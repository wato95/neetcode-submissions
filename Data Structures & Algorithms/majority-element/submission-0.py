class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums) / 2
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > k:
                return i
        