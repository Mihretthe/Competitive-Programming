class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def condition(word):
            return int(word[0] in "aeiou" and word[-1] in "aeiou")
        
        prefix = []

        for word in words:
            prefix.append(condition(word))
        length = len(prefix)
        for i in range(length - 1):
            prefix[i + 1] += prefix[i]
        
        for l, r in queries:
            if l == 0:
                yield prefix[r]
            else:
                yield prefix[r] - prefix[l - 1]