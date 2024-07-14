static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        int minLength   = INT_MAX;
        int totalSum    = 0;
        int leftPointer = 0;

        for(int i=0; i<nums.size(); i++){
            totalSum += nums[i];
            while(totalSum >= target){
                minLength = min(minLength, (i - leftPointer) + 1);
                totalSum = totalSum - nums[leftPointer];
                leftPointer++;
            }
        }

        if(minLength == INT_MAX){
            return 0;
        }
        
        return minLength;
    }
};

