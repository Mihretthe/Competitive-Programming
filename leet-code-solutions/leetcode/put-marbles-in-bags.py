class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        length = len(weights)
        pairs = []

        for i in range(length - 1):
            pairs.append(weights[i] + weights[i + 1])

        k -= 1
        pairs.sort()
        maxi = sum(pairs[length - k - 1:])
        mini = sum(pairs[:k])
        return maxi - mini