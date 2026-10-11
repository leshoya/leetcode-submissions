class ListNode:
    def __init__(self, key=-1,val=-1,next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self, capacity = 8):
        self.map = [ListNode() for i in range(capacity)]
        self.entries = 0

    def index(self,key):
        return key % len(self.map) 
    
    def resize(self):
        old = self.map 
        self.map = [ListNode() for _ in range(len(self.map) * 2)]
        for head in old:
            cur = head.next
            while cur:
                nxt = cur.next
                i = self.index(cur.key)
                cur.next = self.map[i].next
                self.map[i].next = cur 
                cur = nxt
            

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.index(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)
        self.entries += 1
        if (self.entries / len(self.map) > .75):
            self.resize()

    def get(self, key: int) -> int:
        cur = self.map[self.index(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next 
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.index(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.entries -= 1
                return
            cur = cur.next
        
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)