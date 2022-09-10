class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        max_=0
        min_=0
        count=0
        while max_< time:
            for s,e in clips:
                if s <= min_ and e > max_:
                    max_= e
            
            if min_==max_:
                return -1
            min_=max_
            count += 1
        return count
