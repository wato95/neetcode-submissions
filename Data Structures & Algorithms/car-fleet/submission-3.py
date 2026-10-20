class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        times = [(position[i], speed[i], (target - position[i]) / speed[i]) for i in range(len(position))]

        sort_times = sorted(times, key=lambda x: x[0], reverse=True)
        

        for i in sort_times:
            if st and i[2] > st[-1]:
                st.append(i[2])
            if not st:
                st.append(i[2])
        
        return len(st)

