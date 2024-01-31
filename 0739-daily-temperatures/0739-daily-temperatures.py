class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # st = []
        # n = len(temperatures)
        # ans = []
        # for i in range(n-1, -1, -1):
        #     curr = temperatures[i]
        #     # print(curr, st)
        #     count = 0
        #     while st and st[-1][0]<=curr:
        #         st.pop()
        #     # print(st)
        #     if st:
        #         ans.append(st[-1][1]-i)
        #     else:
        #         ans.append(0)
        #     # print(ans)
        #     # print()
        #     st.append((curr, i))
        # return ans[::-1]
        st = []
        ans = []
        
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while st:
                if st[-1][0]>temp:
                    break
                st.pop()
            if st:
                ans.append(st[-1][1]-i)
            else:
                ans.append(0)
            st.append((temp, i))
        return ans[::-1]