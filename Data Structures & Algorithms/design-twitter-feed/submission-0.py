class Twitter:

    def __init__(self):

        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followeeMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time = self.time - 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        ans = []
        minheap = []

        self.followeeMap[userId].add(userId)
        for followeeId in self.followeeMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][idx]
                minheap.append([time, tweetId, followeeId, idx - 1])
        
        heapq.heapify(minheap)
        while minheap and len(ans)<10:
            time, tweetId, followeeId, idx = heapq.heappop(minheap)
            ans.append(tweetId)

            if idx > -1:
                time, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minheap, [time, tweetId, followeeId, idx - 1])

        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
        
