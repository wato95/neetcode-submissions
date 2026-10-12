class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #print(ord('z'), ord('a'), ord('Z'), ord ('A'), ord('9'), ord('0'))

        chars = set(list(range(ord('a'), ord('z') + 1)) +
         list(range(ord('A'), ord('Z') + 1)) +
         list(range(ord('0'), ord('9') + 1)))

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not ord(s[l]) in chars:
                l += 1
            while r > l and not ord(s[r]) in chars:
                r -= 1
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            
            else:
                return False
            
        return True