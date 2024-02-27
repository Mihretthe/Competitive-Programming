class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        current = [1]
        previous = self.generate(numRows - 1)
        the_before = previous[-1]
        for i in range(numRows - 2):
            current.append(the_before[i] + the_before[i + 1])
        current.append(1)

        return previous + [current]

