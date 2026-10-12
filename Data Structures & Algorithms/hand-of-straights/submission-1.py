class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #rearrange the cards into groups so that each group is of size groupsize and card values consecutively increase by 1
        #first we can just use a dictionary and another data structure
        #the dictionary can count how many of each we have
        #need a way to see if we have ever number in sorted order.
        #we can use an array and sort it at the end (o(nlogn))
        #at that point,might as well iterate through the array
        #maybe use a dictionary to a linkedlist. Create Nodes, and if that Node exists, we can iterate through it
        #track the min and max number
        #iterate through and see if we have it. 

        cardCounter = defaultdict(int)

        minCard = hand[0]
        maxCard = hand[0]
        for card in hand:
            cardCounter[card] += 1
            
        #you HAVE to start at the mincard no matter what. 
        #idea is to start at the mincard, and keep going
        #what if we dont have the mincard? First, we can start at the max card. 
        #we can chose a random number
        #what if we choose a random number and go to the bottom. Then, we start it and track the consecutive sequence. We visit each value only twice so we are good. 

        for key in cardCounter: 
            if cardCounter[key] == 0:
                continue

            currMin = key

            while currMin - 1 in cardCounter and cardCounter[currMin-1] > 0:
                currMin = currMin - 1
            while currMin <= key:
                if cardCounter[currMin] == 0:
                    currMin += 1
                    continue
                for i in range(groupSize):
                    cardCounter[currMin+i] -= 1
                    if cardCounter[currMin+i] < 0:
                        return False


        for key, val in cardCounter.items():
            if val != 0:
                return False

        return True            


            
            #get the starting sequence and track min. 
            #remove one from the next groupsizes. 
            #if we have zero left of the card, we move currmin up till cardCounter[key]
            #keep making sequences. 
            #




        