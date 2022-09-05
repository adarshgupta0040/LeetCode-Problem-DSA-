# Using Heap :

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    minheap=[]
    ans=[]
    for i in range(len(arr)):
        diff = abs(x-arr[i])
        heapq.heappush(minheap,[diff,arr[i]])
    print(minheap)                            # [[0, 3], [1, 4], [1, 2], [2, 1], [2, 5]]

    for i in range(k):
        diff,val=heapq.heappop(minheap)
        ans.append(val)
    ans.sort()
    print(ans)                                # [1,2,3,4]

    return ans
