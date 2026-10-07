class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
            
        l, r = 0, len(numbers) - 1

        while l < r:
            lr_sum = numbers[l] + numbers[r]

            if lr_sum == target:
                return [l+1, r+1]
            elif lr_sum > target:
                r -= 1
                continue
            else:
                l += 1
            