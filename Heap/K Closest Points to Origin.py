# Brute Force : O(N log N) + O(K)

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    ans=[]
    temp=[]
    for x,y in points:
        dist= x**2 + y**2
        temp.append([dist,[x,y]])
    #print(temp)                                        [[10, 1, 3], [8, -2, 2]]
    temp.sort()
    #print(temp)                                        [[8, -2, 2], [10, 1, 3]]
    for i in range(k):
        ans.append(temp[i][1])
    return ans
  
  
  
# Optimised : O(K log N)

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    minheap=[]  
    for x,y in points:
        dist= x**2 + y**2
        minheap.append([dist,[x,y]])     
    # print(minheap)                      [[10, 1, 3], [8, -2, 2]]

    heapq.heapify(minheap)
    # print(minheap)                      [[8, -2, 2], [10, 1, 3]]

    ans=[]
    while k:
        dist,points=heapq.heappop(minheap)
        ans.append(points)
        k-=1
    return ans
