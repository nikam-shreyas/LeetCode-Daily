import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':lambda x1, x2:int(x1/x2)
              }
        st = []
        for token in tokens:
            if token not in ops:
                st.append(int(token))
            else:
                
                num2 = st.pop()
                num1 = st.pop()
                st.append(ops[token](num1, num2))
        return st.pop()