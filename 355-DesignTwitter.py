import collections
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        self.tweets[userId].append([tweetId, self.count])
        self.count+=1
        #print self.tweets

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        news = []
        i = 0
        users = []
        if userId in self.followers:
            users = list(self.followers[userId])
        users.append(userId)
        all_news = []
        for user in users:
            all_news+=self.tweets[user]
        all_news = sorted(all_news,key=lambda x:x[1], reverse=True)
        length = 10 if len(all_news)>=10 else len(all_news)
        return [all_news[x][0] for x in range(length)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId==followeeId: return
        self.followers[followerId].add(followeeId)
        #print self.followers

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



        # Your Twitter object will be instantiated and called as such:
        # obj = Twitter()
        # obj.postTweet(userId,tweetId)
        # param_2 = obj.getNewsFeed(userId)
        # obj.follow(followerId,followeeId)
        # obj.unfollow(followerId,followeeId)