class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right

    #remove at left
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #add at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        nxt.prev = prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
            return

        if len(self.cache) >= self.capacity: 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        new = Node(key,value)
        self.insert(new)
        self.cache[key] = new


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)