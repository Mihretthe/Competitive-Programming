class FrequencyTracker:

    def __init__(self):
        self.array = []
        self.freq = {}
        self.vals = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.array.append(number)
        if number in self.freq:
            self.vals[self.freq[number]] -= 1
            self.freq[number] += 1
        else:
            self.freq[number] = 1
        self.vals[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.array.remove(number)
            self.vals[self.freq[number]] -= 1
            self.freq[number] -= 1
            if self.freq[number] == 0:
                self.freq.pop(number)
            else:
                self.vals[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.vals[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)