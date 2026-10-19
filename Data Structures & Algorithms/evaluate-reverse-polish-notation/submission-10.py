class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        ops = {'+': '+', '-':'-', '*':'*', '/':'//'}

        for i in tokens:
            if i in ops:
                rhs = st.pop()
                lhs = st.pop()

                if i == '+':
                    st.append(lhs + rhs)

                elif i == '-':
                    st.append(lhs - rhs)

                elif i == '*':
                    st.append(lhs * rhs)

                elif i == '/':
                    st.append(int(lhs/rhs))
            else:
                st.append(int(i))
        
        return int(st.pop())

