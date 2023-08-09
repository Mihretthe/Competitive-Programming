class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        idx = [l.index(i) for i in s]
        track = [0] * n
        for i in shifts:
            start, end, direction = i
            if direction == 1:
                track[start] += 1
                if  end + 1 < n:
                    track[end + 1] -= 1
            else:
                track[start] -= 1
                if  end + 1 < n:
                    track[end + 1] += 1
        for i in range(1, n):
            track[i] += track[i - 1] 
        ans = ""  
        for i in range(n):
            ans += l[(track[i] + idx[i])% 26]
        return ans
        