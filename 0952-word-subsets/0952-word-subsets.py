class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        answer = []

        counter = Counter()

        for word in words2:
            count = Counter(word)
            for i in count:
                counter[i] = max(counter[i], count[i])

        for word in words1:
            count = Counter(word)

            for i in counter:
                if count[i] < counter[i]:
                    break
            else:
                answer.append(word)
            
        return answer
    