class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        length = len(s)
        left = 0
        right = 0
        indices = defaultdict(int)

        for i in range(length):
            if s[i] in indices:
                indices[s[i]][1] = i
            else:
                indices[s[i]] = [i,i]
        ans = []
        for i in range(length):
            if indices[s[i]][0] > right:
                ans.append(right - left + 1)
                left = right + 1
                right = right + 1
            right = max(indices[s[i]][1], right)

        ans.append(right - left + 1)

        return ans