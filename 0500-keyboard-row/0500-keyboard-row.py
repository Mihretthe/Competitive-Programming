class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]

        answer = []


        for word in words:
            num = -1
            for letter in word:
                my_num = -1
                for i in range(3):
                    row = keyboard[i]
                    if letter in row:
                        my_num = i
                        if num == -1:
                            num = i
                        break
                if num != my_num:
                    break
            else:
                answer.append(word)


        return answer 


