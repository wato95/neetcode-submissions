
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        st = []
        
        opens = set(['(', '[', '{'])
        closes = {'}': '{', ']': '[', ')':'('}

        for i in s:
            if i in opens:
                st.append(i)
            else:
                if st and closes[i] == st[-1]:
                    st.pop()
                else:
                    return False
        
        if len(st) > 0:
            return False
        else:
            return True