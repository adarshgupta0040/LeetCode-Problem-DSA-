#Intuition
  Brute Force

#Approach
  Keep records of losing players with help of dict/Map.
  Now Iter on Matches list & check that who has loss only 1 time & which(winners) are not present in the map/dict 
  also put in that winner in the dict so that if further repeated then we dont take in winners list.

#Complexity
  Time complexity: O(N)
  Space complexity: O(N)
  
  
#Code

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for i in matches:
            print(i[1])
            if i[1] not in d:
                d[i[1]]=1
            else:
                d[i[1]]+=1

        winner=[]
        losser=[]
        for i in matches:
            if d[i[1]]==1:
                losser.append(i[1])
            if i[0] not in d:
                winner.append(i[0])
                d[i[0]]=2

        winner.sort()
        losser.sort()
        return [winner,losser]

      
      
