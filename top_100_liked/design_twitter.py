from collections import deque
from heapq import heappop, heappush, heapify
​
class mydict(dict):
    def __missing__(self, key):
        self[key] = set([key])
        return self[key]
    
class Twitter:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(lambda: deque())
        self.follower = mydict()
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1
        if(len(self.tweets[userId]) > 10):
            self.tweets[userId].popleft()
    
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result, h = [], []
        ### O(n)
        for idx in list(self.follower[userId]):
            if(len(self.tweets[idx])):
                tweetId, timestamp = self.tweets[idx][-1]
                h.append((-timestamp, tweetId, idx, -1))
        ### O(n)
        heapify(h)
        ### O(logn * 10)
        while(len(result) < 10 and len(h) > 0):
            timestamp, tweet, uid, num = heappop(h)
            result.append(tweet)
            if(len(self.tweets[uid]) + num > 0):
                tweetId, timestamp = self.tweets[uid][num-1]
