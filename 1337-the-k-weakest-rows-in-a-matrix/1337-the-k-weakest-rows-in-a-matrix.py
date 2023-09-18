class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counter = [[mat[i].count(1), i] for i in range(len(mat))]
        counter.sort()
        ans = []
        for i in range(k):
            ans.append(counter[i][1])
        return ans
    