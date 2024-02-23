class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = deque()

        deck.sort(reverse = True)

        for card in deck:
            if answer:
                answer.appendleft(answer.pop())
            answer.appendleft(card)

        return answer
        