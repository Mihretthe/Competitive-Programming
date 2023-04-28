class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        for i in words[left:right+1]:
            if i[0] in vowel and i[-1] in vowel:
                c+=1
                
        return c