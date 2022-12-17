class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        st = []
        def isOp(op):
            if op in ['+' ,'-' ,'/', '*']:
                return True
            return False
        
        def doOp(num2, num1, op):
            if op=='+':
                return num1+num2
            elif op=='-':
                return num1-num2
            elif op=='*':
                return num1*num2
            elif op=='/':
                return int(num1/num2)
            
        while True:
            if i==len(tokens):
                break
                
            # print(tokens[i], st)
            if isOp(tokens[i]):
                num1 = st.pop()
                num2 = st.pop()
                op = tokens[i]
                st.append(doOp(num1, num2, op))
            else:
                st.append(int(tokens[i]))
            i+=1
            
        return st[0]
            
            