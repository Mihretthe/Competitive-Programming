class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        count_T = 0
        count_F = 0
        l = 0
        r = 0
        max_len = 0

        for r in range(n):
            if answerKey[r] == "T":
                count_T += 1
            else:
                count_F += 1

            while min(count_T, count_F) > k:
                if answerKey[l] == "T":
                    count_T -= 1
                else:
                    count_F -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len