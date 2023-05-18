class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a = set(i for e in edges for i in e)
        s=set(x[1] for x in edges)
        return list(a-s)