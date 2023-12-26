class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr = []
        counter = Counter(arr1)
        for i in arr2:
            new_arr += [i] * counter[i]

        new_arr += sorted([i for i in arr1 if i not in set(arr2)])

        return new_arr

        
