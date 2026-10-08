#simplified version of twitter which allows users to post, follow/unfollow, and view the 10 most recent tweets within their own feed.

#post tweet -> userID posts tweetID
#getnewsfeed fetches the most 10 recent tweet ID's, its the 10 most recent tweets in their feed
#void follow
#void unfollow 
#First of all, we need to track who each person is following. We can use a set for this for easy add and remove. 
#so, maybe we can have a dictionary of sets. The dictionary is of the users. And the set is of who each user is following 
#-> dictr[user1] = set(user2, user3, user4) *dont forget to add themselves
#this way add and pop is o(1)
#my first idea for getNewsFeed is to just create a list of all the most recent posts, if that user is in the current users dict, we add it to the feed. Otherwise, we keep going
#if we run out, they are done. 
#o(totalfeedsize)
#we can also add a followees set, and then keep a queue for each user. 
#run cost is O(tweets)
#storage cost is o(users*users)
#maybe runtime can be in terms of users
#if user 1 follows user 2. Now if they follow 3, we want to add user 3 to their posts too. 
#If we track the user3 post, we can use a minheap sorted by time added and then add it

#Class needs to track time(when heap is added)
#followers list 
#most recent feed for each user(use a dictionary to a heap again)
#10 most recent posts dict to a (queue)
#so if postTweet(go through the entire followers list and add) so this is just followerslistSize *log10
#follow a user means we iterate through our list and heappush every index and make sure length is less than 10 (we can use a while condition to make this more efficient)
#the unfollow makes it a little more complicated. We will need to find a way to populate the newer posts. First idea is to 

import heapq
from collections import deque
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        #each user in the dict to a set of people they are following 
        self.posts = defaultdict(deque)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        userID = userId
        self.posts[userID].append((-1 * self.time, tweetId, userID))
        self.time += 1
        if(len(self.posts[userID]) > 10):
            self.posts[userID].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        #go through each userIDs following, make a heap and add one. 
        #if we use one say from user2, then add the next most recent post from user2. If there is none, dont add
        #if heap is empty, just dont add anything and return
        #my one issue is how do we track which number we are on on each heap. First idea is to use a dict, and the idx we are on is len(heap) - 1 as the default. if < 0, we cant add anything, othetwise add that index
        userID = userId
        recencyLevel = defaultdict(int)
        #first we are populating where in the list we are since we do not want to pop from the userposts list in the main or make a opy and waste space
        for userFollowed in self.following[userID]:

            recencyLevel[userFollowed] = len(self.posts[userFollowed]) - 1
        recencyLevel[userID] = len(self.posts[userID]) - 1     
        feed = []
        for userInFeed in self.following[userID]:
            if recencyLevel[userInFeed] >=0:
                userPosts = self.posts[userInFeed]
            feed.append(userPosts[recencyLevel[userInFeed]])
        
        if recencyLevel[userID] >= 0:
            userPosts = self.posts[userID]
            feed.append(userPosts[recencyLevel[userID]])
        heapq.heapify(feed)
        last10 = []
        while len(last10) < 10 and feed:
            time, tweet, tweeter = heapq.heappop(feed)
            last10.append(tweet)
            recencyLevel[tweeter] -= 1
            recency = recencyLevel[tweeter]
            if recencyLevel[tweeter] >= 0:
                heapq.heappush(feed, self.posts[tweeter][recency])
        return last10



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
