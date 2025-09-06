class Package:
    def __init__(self, pid, weight, value, priority, destination):
        self.id = pid
        self.weight = weight
        self.value = value
        self.priority = priority
        self.destination = destination 

class Van:
    def __init__(self, vid, capacity):
        self.id = vid
        self.capacity = capacity
