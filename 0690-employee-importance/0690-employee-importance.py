"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        first find the employee by id
        then add the importance to the ans
        then add the importance of its subordinates
        visited = []
        add the items in the visited 
        and one by one add the importance to the ans
        """
        """
        [1,2,3]
        pop 3 [3]
        then add the importance of 3
        ans = 4
        then add the subs to the visited
        [1,2] 
        pop 2 [3,2]
        then add the importance of 2
        ans = 6
        then add the subs to visited
        [1,4] 
        pop 4 [3,2,4]
        add the importance of 4
        ans = 7
        add the subs to visited 
        [1] 
        pop 1 [3,2,4,1]
        add the importance of 1
        ans = 13
        if list(s) and idList == return ans
        
        
        """
        visited = []
        visited.append(id)
        idList = [i.id for i in employees]
        trav = set()
        def visit(ans, id):
            nonlocal visited
            if len(visited) == 0:
                return ans
            
            idx = idList.index(id)
            obj = employees[idx]
            sub = obj.subordinates
            visited += sub
            used = visited.pop()
            trav.add(used)
            ans += employees[idList.index(used)].importance
            return visit(ans, used)
            
            
            

        return visit(0, id)
                
                        