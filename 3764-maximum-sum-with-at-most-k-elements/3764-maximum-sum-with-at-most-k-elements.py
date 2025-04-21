class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # number of rows and number is cols
        rows = len(grid)
        cols = len(grid[0])

        # sort all the rows
        for i in range(rows):
            grid[i].sort(reverse = True)
        
        
        # create heap to have the k most
        heap = []

        # populating the heap
        for i in range(rows):

            # iterating until the limits only

            for j in range(limits[i]):
                heappush(heap, grid[i][j])
                if len(heap) > k:
                    heappop(heap)

        return sum(heap)
