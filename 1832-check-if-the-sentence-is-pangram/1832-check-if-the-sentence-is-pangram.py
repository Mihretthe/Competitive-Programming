class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        for i in string.ascii_lowercase:
            if i in sentence:
                continue
            else:
                return False
        return True