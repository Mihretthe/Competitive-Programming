class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        length = len(answers)
        
        answers.sort()
        left_out = 0
        left = answers[0]

        for i in range(1,length):
            if answers[i] != answers[i - 1]:
                left_out += left
                left = 0

            if answers[i] == answers[i - 1] and left:
                left -= 1
            else:
                left = answers[i]
            
      
        return left_out + length + left 