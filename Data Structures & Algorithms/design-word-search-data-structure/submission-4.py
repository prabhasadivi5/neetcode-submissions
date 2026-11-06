
#data structure that supports adding new words and searching for existing words
#so we can add a word to the structure -> 
#search returns true if there is any string that matches word or false otherwise
#the trick is that we can have a dot that can be matched with any letter
#the first idea is to bruteforce it. If we search for a word with a dot, we can replace it with any letter (26).
#the runtime for this is 26*len(word) at the max but, if its all dots, we have 26^len word
#maybe we can do this a little faster. 
#a tree data structure maybe would reduce it. 
#because at each . , we have at max 26 to match -> middle case is a lot lower 
#the max of this is (all dots) just the size of the dictionary or the length of whatever we have. However, if we have a dot we need to search the next one. We can just use a iterative dfs
#

#1)we need to make our data structure. That has a pointer to it and has a bunch of nodes in it
#we can do a set of nodes. 
#1)If the letter not there, we add it to the current set of nodes (start at the rootSet)
#2)then, we iterate through and keep adding to next
#3(if the new set doesnt exist, we keep adding 
#4)if not, we keep iterating 


#node class has next and cal

class Node: 
    def __init__self(self, val):
        self.nextNode = None
        self.val = val 

class WordDictionary:

    def __init__(self):
        self.headDict = defaultdict(str)
        

    def addWord(self, word: str) -> None:
        #dog 
        #1) iterate through the word
        #2) #first start at the headlist. If the first letter in it, we go to the next. Otherwise, we create a new Node in the set with the value and the currpointer is that
        #3) then we keep iterating and seeing if its there and if not creating a new set and node
        #The issue is that when looking in the set, we have a set of nodes, not values. We can just do dictionaries and key -> Val thats way easier
        #do we even need a node? Why cant we just have a dictionary pointing to a dictionary? 
        #If we were to track suffixes or work backwards, then nodes could be useful maybe? but for now we dont need. We can just do a dictionary to a dictionary. 


        #currDict : Dictionary of Letters, True/False -> Dictionary of Letters w True/False
        #need a way to tag if something is a word and not a substring
        #easiest way is to use a tuple and the second in the dictionary can be whether its a word or not 
        currDict = self.headDict
        for i, letter in enumerate(word):
            if letter in currDict:
                if i == len(word) - 1:
                    currDict[letter]= (currDict[letter][0], True)
                    break
                currDict = (currDict[letter][0])
                
                continue
            else:
                
                currDict[letter] = (defaultdict(str), False)
                if i == len(word) - 1:
                    currDict[letter] = (currDict[letter][0],True)
                    break
                currDict = currDict[letter][0]
        

        
        
    def dfs(self, substr, currDict):
        #1) check if we at the base case (empty string)
        
        #2) check if valid (if not a dot and our dict doesnt work, we fail, otherwise, run recursively with substr)
        #3) run dot forloop check (if we ahve a dot, loop through the entire dict and go, if dict is empty return false.)
        #4)Shouldnt be any case here. The dot check should return true or false 
        
        if substr[0] != "." and substr[0] not in currDict:
            return False 

        if len(substr) == 1 and substr[0] == ".":
            for key, val in currDict.items():
                if currDict[key][1] == True:
                    return True
            return False

        if len(substr) == 1 and substr[0] != ".":
            if currDict[substr[0]][1] == True:
                return True
            return False

        if substr[0] != "." and substr[0] in currDict:
            return self.dfs( substr[1:], currDict[substr[0]][0])
        else:
            passed = False
            for key, val in currDict.items():
                passed = self.dfs( substr[1:], currDict[key][0])
                if passed:
                    return True
            return False 

    def search(self, word: str) -> bool:
        return self.dfs(word, self.headDict)




    

        
