class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half, right_half):
            i = 0
            j = 0
            ans = []
            length1 = len(left_half)
            length2 = len(right_half)

            while i < length1 or j < length2:
                if i == length1:
                    ans.append(right_half[j])
                    j += 1
                    continue
                
                if j == length2:
                    ans.append(left_half[i])
                    i += 1
                    continue
                
                if left_half[i] < right_half[j]:
                    ans.append(left_half[i])
                    i += 1
                else:
                    ans.append(right_half[j])
                    j += 1

            return ans
        

        def mergeSort(nums, left, right):
            if left == right:
                return [nums[left]]

            

            mid = (left + right) // 2
            left_half = mergeSort(nums, left, mid)
            right_half = mergeSort(nums, mid + 1, right)

            return merge(left_half, right_half) 

        length = len(nums) - 1
        return mergeSort(nums, 0, length)