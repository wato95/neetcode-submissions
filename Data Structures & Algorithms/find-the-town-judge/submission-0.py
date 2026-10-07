class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusted = set()
        people = set([i for i in range(1, n+1)])

        for a, b in trust:
            people.remove(a)
            trusted.add(b)
            if len(trusted) > 1:
                return -1
        
        else:
            return people.pop()

