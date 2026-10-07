class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {nums[i]:i for i in range(len(nums))}

        for i, n in enumerate(nums):
            other_value = target - n
            if other_value in check.keys():
                k = check[other_value]
                if i != k:
                    if i < k:
                        return [i, k]
                    else:
                        return [k,i]