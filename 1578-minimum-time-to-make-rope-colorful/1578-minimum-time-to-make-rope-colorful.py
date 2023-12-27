class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        st = [0]
        time = 0
        for i in range(1, len(colors)):
            if colors[i]==colors[st[-1]]:
                if neededTime[st[-1]]<neededTime[i]:
                    time+=neededTime[st[-1]]
                    st.pop()
                    st.append(i)
                else:
                    time+=neededTime[i]
            else:
                st.append(i)
        return time
                    