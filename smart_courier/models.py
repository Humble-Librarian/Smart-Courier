
class Package:
    def __init__(self, pid, weight, value, priority=1):
        self.id = pid; self.weight = weight; self.value = value; self.priority = priority
    def __repr__(self): return f"Package(id={self.id}, w={self.weight}, v={self.value}, p={self.priority})"

class Van:
    def __init__(self, vid, capacity=50):
        self.id = vid; self.capacity = capacity
    def __repr__(self): return f"Van(id={self.id}, cap={self.capacity})"
