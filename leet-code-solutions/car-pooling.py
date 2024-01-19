class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[2])
        length = trips[-1][2]
        trips.sort(key = lambda x : x[1])
        length = max(length, trips[-1][1])
        
        prefix = [0] * length

        for num, start, end in trips:
            prefix[start] += num
            if end < length:
                prefix[end] -= num
        if prefix[0] > capacity:
            return False

        for i in range(1, length):
            prefix[i] += prefix[i - 1]
            if prefix[i] > capacity:
                return False

        return True

        