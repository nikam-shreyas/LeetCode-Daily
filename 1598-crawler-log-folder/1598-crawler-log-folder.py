class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for log in logs:
            if log=='../':
                if st!=[]:
                    st.pop()
            elif log=='./':
                pass
            else:
                st.append(log)
        return len(st)
                    