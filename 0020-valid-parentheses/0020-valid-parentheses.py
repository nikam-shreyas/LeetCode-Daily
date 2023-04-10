class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openb = {'[':']', '{':'}', '(':')'}
        for char in s:
            if char in openb:
                st.append(char)
            else:
                if st == []:
                    return False
                elif openb[st[-1]]!=char:
                    return False
                else:
                    st.pop()
        if st==[]:
            return True
        return False