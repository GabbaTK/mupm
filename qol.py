class LoopedList(list):
    def __init__(self, iterable=[]):
        super().__init__(iterable)
        self.idx = 0

    def __getitem__(self, idx: int):
        prefix = idx / abs(idx)
        normalized = abs(idx) % len(self)
        prefix_normalized = int(normalized * prefix)
    
        return super().__getitem__(prefix_normalized)
    
    def __setitem__(self, idx: int, val):
        prefix = idx / abs(idx)
        normalized = abs(idx) % len(self)
        prefix_normalized = int(normalized * prefix)
    
        super().__setitem__(prefix_normalized, val)
    
    def next(self):
        self.idx += 1
        prefix = (self.idx + len(self)) / (abs(self.idx) + len(self))
        normalized = abs(self.idx) % len(self)
        prefix_normalized = int(normalized * prefix)
        self.idx = prefix_normalized
    
        return super().__getitem__(prefix_normalized)
    
    def prev(self):
        self.idx -= 1
        prefix = (self.idx + len(self)) / (abs(self.idx) + len(self))
        normalized = abs(self.idx) % len(self)
        prefix_normalized = int(normalized * prefix)
        self.idx = prefix_normalized
    
        return super().__getitem__(prefix_normalized)
    
    def cur(self):
        return super().__getitem__(self.idx)
