class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = blocks[:k].count('W')
        min_operation = count



        for start in range(1, len(blocks) - k + 1):
            if blocks[start - 1] == "W":
                count -= 1
            if blocks[start + k - 1] == "W":
                count += 1
            min_operation = min(count, min_operation)


        return min_operation
