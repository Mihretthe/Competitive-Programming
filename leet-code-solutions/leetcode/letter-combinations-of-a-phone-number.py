class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        path = []
        digit = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
            }

        def backtrack(index):
            if len(path) == len(digits):
                if path:
                    answer.append("".join(path))
                return 
            
            for i in range(len(digit[digits[index]])):
                path.append(digit[digits[index]][i])
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return answer
