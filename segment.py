class SegmentTree:

    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.tree = [0] * (2 * self.length)
        self.build()

    def build(self):
        # for i in range(self.length, len(self.tree)):
        #     self.tree[i] = self.array[i - self.length]

        for i in range(self.length):
            self.tree[i + self.length] = self.array[i]

        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i]

    def update(self, index, value):
        self.array[index] = value
        index = self.length + index
        self.tree[index] = value
        
        while index != 1:
            parent = index // 2
            self.tree[parent] = self.tree[parent * 2] + self.tree[parent * 2 + 1]
            index = parent
            

    def query(self, left, right):
        left += self.length
        right += self.length
        answer = 0

        while left < right:
            if left % 2:
                answer += self.tree[left]
                left = (left + 1) // 2
            else:
                left = left // 2

            if right % 2:
                answer += self.tree[right - 1]
                right = (right - 1) // 2
            else:
                right = right // 2

        return answer
