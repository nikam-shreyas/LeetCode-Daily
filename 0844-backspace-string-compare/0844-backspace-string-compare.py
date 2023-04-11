class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        for char in s:
            if st1!=[] and char=='#':
                st1.pop()
            elif char!='#':
                st1.append(char)
        st2 = []
        
        for char in t:
            if st2!=[] and char=='#':
                st2.pop()
            elif char!='#':
                st2.append(char)
        # print(st1, st2)
        return st1==st2