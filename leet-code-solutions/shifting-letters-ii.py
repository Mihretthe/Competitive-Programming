class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        indices = []
        length = len(s)

        for i in range(length):
            indices.append(letters.index(s[i]))
        prefix = [0] * length

        for shift in shifts:
            start, end, dxn = shift
            if dxn == 1:
                prefix[start] += 1
                if end + 1 < length:
                    prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                if end + 1 < length:
                    prefix[end + 1] += 1
        for i in range(1, length):
            prefix[i] += prefix[i - 1]

        ans = []

        for i, j in zip(prefix, indices):
            ans.append(letters[(i + j) % 26])

        return "".join(ans)
