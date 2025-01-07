class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        answer = []
        for word in words:
            count = -1
            for word2 in words:
                if word in word2:
                    count += 1
                if count > 0:
                    answer.append(word)
                    break
        
        return answer