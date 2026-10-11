class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        tot = 0

        while r > l:
            tot = numbers[l] + numbers[r]

            if tot < target:
                l += 1
            
            elif tot > target:
                r -= 1
            
            elif tot == target:
                return [l + 1, r + 1]
