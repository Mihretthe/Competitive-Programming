class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        letters-sorted
        character-target
        there are at least two different characters in letters              
        """
        # s="abcdefghijklmnopqrstuvwxyz"
        for i in letters:
            if i>target:
                return i 
        return letters[0]