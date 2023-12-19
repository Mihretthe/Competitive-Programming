class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        dxn = [[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1], [0,0]]
        ans = []

        for i in range(n):
            row = []
            for j in range(m):
                final_value = 0
                collect = []
                for r, c in dxn:
                    r += i
                    c += j
                    if r >= 0 and c >= 0 and r < n and c < m :
                        collect.append(img[r][c])
                        
                    if collect:
                        final_value = sum(collect) // len(collect)
                row.append(final_value)
            ans.append(row)
        return ans
