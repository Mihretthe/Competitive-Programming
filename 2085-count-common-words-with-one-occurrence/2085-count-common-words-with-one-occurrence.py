class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len([x for x in words1 if x in words2 and words1.count(x)==1 and words2.count(x)==1])