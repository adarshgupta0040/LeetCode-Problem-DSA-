# Brute Force:

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
		int maxlen = 0;
        for (int i = 0; i < nums.size(); i++) {
            int zeroes = 0, ones = 0;
            for (int j = i; j < nums.size(); j++) {
                if (nums[j] == 0) {
                    zeroes++;
                } else {
                    ones++;
                }
                if (zeroes == ones) {
                    maxlen = max(maxlen, j - i + 1);
                }
            }
        }
        return maxlen;
    }
};



# Optimised :

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict1={}
        subarr=0
        count=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            if nums[i]==1:
                count-=1
            if count==0:
                subarr=i+1
            if count in dict1:
                subarr=max(subarr,i-dict1[count])
            else:
                dict1[count]=i
        return subarr
