class Node:
    def __init__(self, value, key, nxt=None, prev=None):
        self.val = value
        self.key = key
        self.next = nxt
        self.prev = prev
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.d        = {}
        self.head     = Node(None,None)
        self.tail     = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        """
        :type capacity: int
        """

    def _append_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if(key not in self.d):
            return -1
        node = self.d[key]
        self._remove_tail(node)
        self._append_head(node)

        return node.val
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        node = Node(value, key)
        if(key in self.d):
            old_node = self.d[key]
            del self.d[key]
            self._remove_tail(old_node)
        self.d[key] = node

        if(len(self.d) > self.capacity):
            del self.d[self.tail.prev.key]
            self._remove_tail(self.tail.prev)

        self._append_head(node)
        """
        :type key: int
        :type value: int
        :rtype: None
