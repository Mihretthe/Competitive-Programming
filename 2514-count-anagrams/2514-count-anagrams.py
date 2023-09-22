class Solution:
    def countAnagrams(self, s: str) -> int:
        s = s.split()
        ans = 1
        for i in s:
            a = Counter(i)
            if len(a) == 1:
                ans *= 1
            else: 
                c = 1
                for j in a:
                    if a[j] > 1:
                        c *= math.factorial(a[j])
                ans *= (math.factorial(len(i)) // c)
        return ans % (10**9 + 7)
                
            