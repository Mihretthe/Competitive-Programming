class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        matrix = []
        rows = len(box)
        cols = len(box[0])
        for row in box:
            fast = cols - 1
            slow = fast

            while fast >= 0:
                if row[fast] == ".":
                    if row[slow] != ".":
                        slow = fast
                    fast -= 1
                elif row[fast] == "*":
                    fast -= 1
                    slow = fast
                else:
                    if row[slow] == ".":
                        row[slow], row[fast] = row[fast], row[slow]
                        fast -= 1
                        slow -= 1
                    else:
                        fast -= 1
            matrix.append(row)
        
        matrix = zip(*matrix[::-1])

        return matrix