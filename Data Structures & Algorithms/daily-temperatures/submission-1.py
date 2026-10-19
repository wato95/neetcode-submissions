class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        st = []
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):

            if not st:
                st.append((val, i))

            else:
                if val <= st[-1][0]:
                    st.append((val, i))
                else:
                    while st and val > st[-1][0]:
                        day = st.pop()
                        res[day[1]] = i - day[1]
                    
                    st.append((val, i))
            

        return res