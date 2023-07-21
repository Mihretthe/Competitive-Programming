class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def frequency(string):
            string = [i for i in string]
            string.sort()
            s = string[0]
            s = string.count(s)
            return s
        que = []
        ans = []
        for i in queries:
            que.append(frequency(i))
        for i in words:
            ans.append((frequency(i)))
        answer = []
        for i in que:
            count  = 0
            for j in ans:
                if j > i:
                    count+=1
            answer.append(count)
        return answer