class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        length = len(path)
        
        index = 0
        while index < length:

            if path[index] == "/":
                index += 1
                s = ""
                while index < length and path[index] != "/":
                    s += path[index]
                    index += 1
                 
                if s:
                    if s == "..":
                        if stack:
                            stack.pop()
                    elif s == ".":
                        continue
                    else:
                        stack.append(s)
            
        

        return "/" + "/".join(stack)