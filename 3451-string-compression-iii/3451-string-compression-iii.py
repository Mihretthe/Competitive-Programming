class Solution:
    def compressedString(self, word: str) -> str:
        
        start = word[0]
        count = 1

        index = 1
        length = len(word)
        ans = []

        while index < length:
            if start == word[index]:
                count += 1
            else:
                if count > 9:
                    new = ["9" + start] * (count // 9)
                    mod = count % 9
                    if mod:
                        new.append(str(mod) + start)
                    ans.extend(new)
                else:
                    ans.append(str(count) + start)
                start = word[index]
                count = 1
            index += 1
        if count > 9:
            new = ["9" + start] * (count // 9)
            mod = count % 9
            if mod:
                new.append(str(mod) + start)
            ans.extend(new)
        else:
            ans.append(str(count) + start)
        
        return "".join(ans)