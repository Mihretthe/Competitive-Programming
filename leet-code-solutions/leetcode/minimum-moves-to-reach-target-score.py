class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        count = 0

        while target > 1:
            if target % 2 == 1:
                target -= 1
                count += 1
            else:
                if maxDoubles:
                    target //= 2
                    count += 1
                    maxDoubles -= 1
                else:
                    count += (target - 1)
                    break
        return count
