class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        """
        [1,3] [2,6]
        check if 3 is >= 2
            list = [min(1,2) , max(3,6)]
            result = [1,6]
            change the value of the intervals[i] and delete the i + 1
        """
        while i < n - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][0] <= intervals[i + 1][0]:
                    a = intervals[i][0]
                else:
                    a = intervals[i + 1][0]
                if  intervals[i + 1][1] >=  intervals[i][1]:
                    b =  intervals[i + 1][1]
                else:
                    b =  intervals[i][1]
                intervals[i] = [a,b]
                intervals = intervals[:i + 1] + intervals[i + 2:]
                n -= 1
            else:
                i += 1
        return intervals
                
            