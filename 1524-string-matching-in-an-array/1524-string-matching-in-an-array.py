class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x : len(x))

        length = len(words)
        answer = []

        for i in range(length):
            word = words[i]
            for j in range(i + 1, length):
                if word in words[j]:
                    answer.append(word)
                    break

        return answer

