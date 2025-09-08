# This file defines the basic data structures for packages and vans

class Package:
    # Represents a delivery package in the courier system
    def __init__(self, pid, weight, value, priority, destination):
        # Store package ID (unique identifier)
        self.id = pid
        # Store package weight in kg
        self.weight = weight
        # Store package value/importance
        self.value = value
        # Store delivery priority (1-5, 5 being highest)
        self.priority = priority
        # Store destination location code
        self.destination = destination 

class Van:
    # Represents a delivery van in the courier system
    def __init__(self, vid, capacity):
        # Store van ID (unique identifier)
        self.id = vid
        # Store maximum weight capacity in kg
        self.capacity = capacity
