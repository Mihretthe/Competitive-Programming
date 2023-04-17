class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or  word==word[0].upper()+word[1:].lower() or word==word.lower():
            return True
        else:
            return False