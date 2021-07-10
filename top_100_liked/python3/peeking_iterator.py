# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
​
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        ### there is always at least one number in nums
        self.nxt = iterator.next()
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        ### since all call to peek is valid we just return the nxt
        return self.nxt
​
    def next(self):
        """
        :rtype: int
        """
        tmp = self.nxt
        if(self.iterator.hasNext()):
            self.nxt = self.iterator.next()
        else:
            self.nxt = None
        return tmp
​
    def hasNext(self):
        """
        :rtype: bool
