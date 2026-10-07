class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            l_char = s[lp].lower()
            r_char = s[rp].lower()

            if l_char.isalnum():
                if r_char.isalnum():
                    if l_char != r_char:
                        return False
                    lp += 1
                    rp -= 1
                else:
                    rp -= 1
            else:
                lp += 1
            
        return True
