class Stats:
    def __init__(self, cumulative_freq: list):
        self.cumulative_freq = cumulative_freq
    
    def less(self, value: int) -> int:
        if value <= 0:
            raise ValueError("Value must be a positive integer.")
        elif value > 1000:
            return self.cumulative_freq[999]
        else:
            return self.cumulative_freq[value - 1]
    
    def greater(self, value: int) -> int:
        if value < 0:
            raise ValueError("Value must be a non-negative integer.")
        elif value >= 1000:
            return 0
        else:
            return self.cumulative_freq[999] - self.cumulative_freq[value]
    
    def between(self, low: int, high: int) -> int:
        if low >= high or low < 0 or high < 0:
            raise ValueError("Invalid range. 'low' should be less than 'high' and both should be non-negative integers.")
        low = max(0, low)
        high = min(999, high)
        if low == 0:
            return self.cumulative_freq[high]
        else:
            return self.cumulative_freq[high] - self.cumulative_freq[low - 1]


class DataCapture:
    def __init__(self):
        self.freq = [0] * 1000
    
    def add(self, value: int):
        if not (0 < value < 1000):
            raise ValueError("Value must be a positive integer less than 1000.")
        self.freq[value] += 1
    
    def build_stats(self) -> Stats:
        cumulative_freq = self.freq.copy()
        for i in range(1, 1000):
            cumulative_freq[i] += cumulative_freq[i - 1]
        return Stats(cumulative_freq)