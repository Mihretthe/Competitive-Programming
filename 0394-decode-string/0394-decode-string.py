class Solution:
    def decodeString(self, s: str) -> str:
        # Intution
        # if number is found 
        #   take that number out 
        #   collect the string inside
        #   call the function for that string again so that we can multiply it by the number

        # if it is normal letter return the later and the rest string with the same function


        if not s:
            return ""
        

        index = 0
        num = []
        while s[index] in "0987654321":
            num.append(s[index])
            index += 1
        
        if num:
            num = int("".join(num))
            string = []
            count = 1
            for i in range(index + 1, len(s)):
                if s[i] == "]":
                    count -= 1
                if count == 0:
                    last = i + 1
                    break
        
                if s[i] == "[":
                    count += 1
                
                string.append(s[i])
            else:
                last = len(s)
            
            string = "".join(string)

            return num * self.decodeString(string) + self.decodeString(s[last:])
        else:
            return s[0] + self.decodeString(s[1:])
                
                
                



