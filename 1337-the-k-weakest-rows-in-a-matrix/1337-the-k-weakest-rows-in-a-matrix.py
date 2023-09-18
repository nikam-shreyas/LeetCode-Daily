class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(sum(row), index) for index, row in enumerate(mat)]
        rows.sort()
        return [row[1] for row in rows][:k]