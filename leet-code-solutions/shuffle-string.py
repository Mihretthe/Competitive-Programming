class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [""] * len(s)

        for idx in range(len(s)):
            shuffled[indices[idx]] = s[idx]

        return "".join(shuffled)