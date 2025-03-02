class Node:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key  # needs key for O(1) deletion from future hashmap we will be using this class with in LRU cache
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node(val={self.val}, key={self.key})"
