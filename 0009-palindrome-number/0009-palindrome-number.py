class Solution:
    def isPalindrome(self, x: int) -> bool:
        # to check if the number is palindrome 
        #  1. change the number to a string : O(log(abs(number))) in base 10
        #  2. check if it is the same forward and backward by using two pointers from the left most and right most

        number = str(x)
        
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] != number[right]:
                return False
            
            # move the colliding pointers
            left += 1
            right -= 1

        return True