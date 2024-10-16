class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heappush(heap, (-a, "a"))
        if b:
            heappush(heap, (-b, "b"))
        if c:
            heappush(heap, (-c, "c"))

        answer = []

        while heap:
            count, letter = heappop(heap)
            count = -count
            if (len(answer) >= 2 and answer[-1] == letter and answer[-2] == letter):
                if not heap:
                    break
                tempCount, tempLetter = heappop(heap)
                answer.append(tempLetter)
                if tempCount + 1 < 0:
                    heappush(heap, (tempCount + 1, tempLetter))
                heappush(heap, (-count, letter))
            else:
                count -= 1
                answer.append(letter)
                if count > 0:
                    heappush(heap, (-count,letter))
        return "".join(answer)

        