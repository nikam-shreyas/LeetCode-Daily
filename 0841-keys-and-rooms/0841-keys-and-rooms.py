class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # start = [0]
        st = [0]
        visited = set()
        visited.add(0)
        while st:
            curr = st.pop()
            for i in rooms[curr]:
                if i not in visited:
                    visited.add(i)
                    st.append(i)
        return len(visited)==len(rooms)