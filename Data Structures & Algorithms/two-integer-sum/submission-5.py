class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            missing = target - val

            if missing in seen:
                return [seen[missing], i]
            else:
                seen[val] = i