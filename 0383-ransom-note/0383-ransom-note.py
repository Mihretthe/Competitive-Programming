class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine=[x for x in magazine]
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True
           