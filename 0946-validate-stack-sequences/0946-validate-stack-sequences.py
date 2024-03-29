class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # i=0
        # j=0
        # st = []
        # while j<len(popped):
        #     if st and st[-1]==popped[j]:
        #         st.pop()
        #         j+=1
        #     elif i<len(pushed) and pushed[i]==popped[j]:
        #         i+=1
        #         j+=1
        #     elif i<len(pushed):
        #         st.append(pushed[i])
        #         i+=1
        #     else:
        #         return False
        # return st==[] 
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)