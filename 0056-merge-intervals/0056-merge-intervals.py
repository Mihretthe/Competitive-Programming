class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        o=[intervals[0]]
        for i, j in intervals[1:]:
            last=o[-1][1]
            if i<=last:
                o[-1][1]=max(last,j)
            else:
                o.append([i,j])
        return o
