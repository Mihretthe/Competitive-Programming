class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        is_comment = False
        length = len(source)
        temp = []
        answer = []

        for i in range(length):
            code = source[i]
            j = 0
            length_of_code = len(code)
            

            while j < length_of_code:
                if j < length_of_code - 1:
                    if is_comment:
                        if code[j] == "*" and code[j + 1] == "/":
                            is_comment = False
                            j += 2
                            continue
                    else:
                        if code[j] == "/":
                            if code[j + 1] == "*":
                                is_comment = True
                                j += 2
                                continue
                            elif code[j + 1] == "/":
                                break
                if not is_comment:
                    temp.append(code[j])
                j += 1

                
            if not is_comment and temp:
                answer.append("".join(temp[:]))
                temp = []

        return answer
                