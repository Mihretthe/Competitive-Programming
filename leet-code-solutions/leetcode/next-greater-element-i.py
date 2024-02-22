class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {key : -1 for key in nums1}
        stack = []

        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                if stack[-1] > nums2[i]:
                    stack.append(nums2[i])
                else:
                    while stack and stack[-1] < nums2[i]:
                        num = stack.pop()
                        if num in hashmap:
                            hashmap[num] = nums2[i]
                    stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(hashmap[num])


        return ans

            
        