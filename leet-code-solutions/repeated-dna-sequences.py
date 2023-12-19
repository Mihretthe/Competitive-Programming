class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        hashmap = defaultdict(int)
        ans = []

        for i in range(n - 9):
            sequence = s[i:i+10]
            hashmap[sequence] += 1
            if hashmap[sequence] == 2:
                ans.append(sequence)

        return ans