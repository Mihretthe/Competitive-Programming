class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in sources:
                return p[1]
            