class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 1, -1):
            max_index = arr.index(max(arr[:i]))
            if max_index != i - 1:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)
                arr[:i] = arr[:i][::-1]
                result.append(i)
        return result