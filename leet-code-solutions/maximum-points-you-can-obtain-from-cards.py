class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        from_start = sum(cardPoints[:k])
        from_end = sum(cardPoints[length - k:])

        start = 0
        end = length - 1
        s = k - 1
        e = length - k
        max_score = 0

        while k and start <= end:
            if from_start == from_end:
                if cardPoints[start] >= cardPoints[end]:
                    max_score += cardPoints[start]
                    from_start -= cardPoints[start]
                    from_end -= cardPoints[e]
                    e += 1
                    start += 1
                elif cardPoints[start] < cardPoints[end]:
                    max_score += cardPoints[end]
                    from_end -= cardPoints[end]
                    from_start -= cardPoints[s]
                    s -= 1
                    end -= 1
            elif from_start > from_end:
                max_score += cardPoints[start]
                from_start -= cardPoints[start]
                from_end -= cardPoints[e]
                e += 1
                start += 1
            else:
                max_score += cardPoints[end]
                from_end -= cardPoints[end]
                from_start -= cardPoints[s]
                s -= 1
                end -= 1
            k -= 1

        return max_score


               





        return 0
