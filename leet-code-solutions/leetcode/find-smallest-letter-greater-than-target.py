class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = -1
        right = len(letters) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid

        if letters[right] > target:return letters[right]
        return letters[0]