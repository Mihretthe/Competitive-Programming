class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a=set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])
        a=list(a)
        s=set(x[1] for x in edges)
        return [i for i in a if i not in s]