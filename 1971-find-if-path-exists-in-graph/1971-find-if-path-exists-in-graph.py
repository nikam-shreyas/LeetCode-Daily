from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        
        if source==destination:
            return True
        if source not in adj_list:
            return False
        
        visited = set()
        visited.add(source)
        st = [source]
        while st:
            curr = st.pop()
            for neighbor in adj_list[curr]:
                if neighbor==destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    st.append(neighbor)
        return False