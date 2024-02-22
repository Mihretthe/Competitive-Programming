class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(0, len(tickets)))
        count = 0

        while tickets[k] > 0:
            index = queue.popleft()
            count += 1
            tickets[index] -= 1
            if tickets[index] != 0:
                queue.append(index)

        return count