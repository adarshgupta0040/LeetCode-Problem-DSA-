class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        maxx=0
        minn=0
        count=0
        while maxx< time:
            for start,end in clips:
                if s <= minn and e > maxx:
                    maxx= end
            
            if minn==maxx:
                return -1
            minn=maxx
            count += 1
        return count
