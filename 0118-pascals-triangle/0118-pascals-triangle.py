class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            a = [1] * (i + 1)
            for j in range(1,i):
                a[j] = ans[i - 1][j] + ans[i - 1][j - 1]
            ans.append(a)
        return ans
        