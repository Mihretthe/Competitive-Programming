class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def nooverlap(lists):
            lists.sort()
            for i in range(len(lists) - 1):
                if lists[i][1] in range(lists[i + 1][0],lists[i + 1][1] + 1):
                    return i
                elif lists[i + 1][0] in range(lists[i ][0],lists[i ][1] + 1):
                    return i
            return -1
        def mergeing(a,b):
            return [a[0],max(a[1],b[1])]
        intervals.sort()
        idx = nooverlap(intervals)
        if idx == -1:
            return intervals
        else:
            intervals[idx] = mergeing(intervals[idx],intervals[idx + 1])
            intervals = intervals[:idx + 1] + intervals[idx + 2:]
            return self.merge(intervals)
                
                
        return []