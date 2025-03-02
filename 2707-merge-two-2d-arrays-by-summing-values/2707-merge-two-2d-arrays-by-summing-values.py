class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        length1 = len(nums1)
        length2 = len(nums2)

        first = 0
        second = 0
        answer = []

        while first < length1 and second < length2:
            id1, val1 = nums1[first]
            id2, val2 = nums2[second]

            if id1 == id2:
                answer.append([id1, val1 + val2])
                first += 1
                second += 1
            elif id1 < id2:
                answer.append([id1, val1])
                first += 1
            else:
                answer.append([id2, val2])
                second += 1
        
        answer.extend(nums1[first:])
        answer.extend(nums2[second:])

        return answer