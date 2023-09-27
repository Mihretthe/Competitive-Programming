class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tape_length = 0
        i = 0

        while i < len(s):
            char = s[i]

            if char.isalpha():
                tape_length += 1
                if tape_length == k:
                    return char
            else:
                repeat = int(char)
                if tape_length * repeat >= k:
                    if k % tape_length == 0:
                        return self.decodeAtIndex(s[:i], tape_length)
                    else:
                        return self.decodeAtIndex(s[:i], k % tape_length)

                tape_length *= repeat

            i += 1

        return ""