from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        st = deque()
        
        opens = set(['(', '[', '{'])
        closes = {'}': '{', ']': '[', ')':'('}

        for i in s:
            if i in opens:
                st.append(i)
            else:
                try:
                    if closes[i] != st.pop():
                        return False
                except:
                    return False
        
        if len(st) > 0:
            return False
        else:
            return True