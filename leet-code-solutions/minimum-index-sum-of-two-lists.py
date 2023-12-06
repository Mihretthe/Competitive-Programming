class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        small_sum = float('inf')
        ans = []

        for idx in range(len(list1)):
            if list1[idx] in list2:
                if idx + list2.index(list1[idx]) < small_sum:
                    ans = [list1[idx]]
                    small_sum = idx + list2.index(list1[idx])
                elif idx + list2.index(list1[idx]) == small_sum:
                    ans.append(list1[idx])
                


        return ans