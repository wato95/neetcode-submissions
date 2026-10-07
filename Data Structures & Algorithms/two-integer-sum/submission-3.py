class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            missing = target - nums[i]

            if missing in seen and seen[missing] != i:
                if i > seen[missing]:
                    return [seen[missing], i]
                else:
                    return [i, seen[missing]]


