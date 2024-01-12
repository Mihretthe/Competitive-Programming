class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indices = {}
        length = len(cards)
        minimum_length = float('inf')

        for index in range(length):
            if cards[index] in indices:
                minimum_length = min(minimum_length, index - indices[cards[index]] + 1)
                indices[cards[index]] = index
            else:
                indices[cards[index]] = index

        if minimum_length == float('inf'):
            return -1
        return minimum_length
