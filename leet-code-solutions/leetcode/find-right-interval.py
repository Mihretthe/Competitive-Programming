class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        ends = []
        length = len(intervals)

        for i in range(length):
            start, end = intervals[i]
            starts.append(start)
            ends.append(end)
        
        original = starts[:]
        starts.sort()
        answer = []

        for end in ends:
            left = 0
            right = len(starts) - 1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid] < end:
                    left = mid + 1
                else:
                    right = mid - 1


            if left >= len(intervals):
                answer.append(-1)
            else:
                answer.append(original.index(starts[left]))

        return answer