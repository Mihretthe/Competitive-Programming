class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = len(answerKey)
        left = 0
        count_true = 0
        count_false = 0
        max_consecutive = 0

        for right in range(length):
            if answerKey[right] == "T":
                count_true += 1
            else:
                count_false += 1
            if min(count_false, count_true) > k:                
                if answerKey[left] == "F":
                    count_false -= 1
                else:
                    count_true -= 1
                left += 1
            max_consecutive = max(max_consecutive, right - left + 1)
        
        return max_consecutive 
                    
