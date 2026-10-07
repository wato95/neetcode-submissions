class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(x, y) for x, y in zip(position, speed)]

        cars.sort(key=lambda x: x[0], reverse=True)
        
        res = []

        for pos, sp in cars:
            time = (target-pos)/sp

            if len(res) == 0:
                res.append(time)
            else:
                if time <= res[-1]:
                    continue
                else:
                    res.append(time)
            
            print(res)

        return len(res)