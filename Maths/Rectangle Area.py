class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaR1=(ax2-ax1)*(ay2-ay1)
        areaR2=(bx2-bx1)*(by2-by1)

        commonX1=max(ax1,bx1)              #for common region both coodinates (X1,Y1) and (X2,Y2)
        commonY1=max(ay1,by1)
        commonX2=min(ax2,bx2)
        commonY2=min(ay2,by2)

        common_Rec_length=commonX2-commonX1
        common_Rec_height=commonY2-commonY1
        common_area= (common_Rec_length * common_Rec_height)

        if common_Rec_length>0 and common_Rec_height>0:
            return areaR1+areaR2-common_area
        else:
            return areaR1+areaR2
