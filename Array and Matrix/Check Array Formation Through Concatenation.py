class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={}
        for i in pieces:
            d[i[0]]=i
        print(d)             #{88: [88], 15: [15]} ,  {78: [78], 4: [4, 64], 91: [91]}
        res=[]
        for i in arr:
            if i in d:
                res.extend(d[i])
        print(res)                    # [15,88] , [91,4,64,78]
        return res==arr
