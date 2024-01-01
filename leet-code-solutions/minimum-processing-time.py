class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        minTime = 0

        for i in range(len(processorTime)):
            minTime = max(minTime, processorTime[i] + tasks[i * 4])

        return minTime


