class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([x for x in words if x==s[:len(x)]])