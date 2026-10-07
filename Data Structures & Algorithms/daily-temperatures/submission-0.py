class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n-1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
                
                while len(stack) > 0:
                    last_temp = stack[-1]
                    if last_temp[0] < temperatures[i+1]:
                        stack.pop()
                        res[last_temp[1]] = i +1  - last_temp[1]
                    else:
                        break

            else:
                stack.append((temperatures[i], i))


            
        
        return res

