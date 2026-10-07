class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        k = 0

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                
            else:
                if k == 0:
                    if s[l] == s[r-1]:
                        l += 1
                        r -= 2
                        k += 1
                    elif s[r] == s[l+1]:
                        l += 2
                        r -= 1
                        k += 1
                    else:
                        return False
                else:
                    return False
        return True
