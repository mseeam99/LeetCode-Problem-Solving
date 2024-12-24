class Twitter:

    def __init__(self):
        self.followAndUnfollow = {}
        self.allTweets = {}
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.allTweets:
            self.allTweets[userId] = []
            self.allTweets[userId].append((self.timestamp*-1,tweetId))
            self.timestamp+=1
        else:
            self.allTweets[userId].append((self.timestamp*-1,tweetId))
            self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        allConnectedUsers = [userId]
        if userId in self.followAndUnfollow:
            allConnectedUsers.extend(self.followAndUnfollow[userId])
        
        feedWithFullOfTweets = []

        for user in allConnectedUsers:
            if user in self.allTweets:
                feedWithFullOfTweets.extend(self.allTweets[user])
   
        answer = []
        copy = feedWithFullOfTweets
        for i in range(min(10,len(feedWithFullOfTweets))):
            heapq.heapify(feedWithFullOfTweets)
            tempTuple = heapq.heappop(feedWithFullOfTweets)
            if tempTuple[1] not in answer:
                answer.append(tempTuple[1])
        feedWithFullOfTweets = copy
        return answer
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followAndUnfollow:
            self.followAndUnfollow[followerId] = []
            self.followAndUnfollow[followerId].append(followeeId)
        else:
            self.followAndUnfollow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followAndUnfollow:
            currentList = self.followAndUnfollow[followerId]
            newList = []
            for i in range(len(currentList)):
                if currentList[i] == followeeId:
                    continue
                else:
                    newList.append(currentList[i])
            self.followAndUnfollow[followerId] = newList
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)