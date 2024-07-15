static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return helper(nums, goal) - helper(nums, goal - 1);
    }

private:
    int helper(vector<int>& nums, int goal) {
        if (goal < 0){
            return 0;
        }

        int leftPointer = 0;
        int tempValue = 0;
        int subarrayCount = 0;

        for(int rightPointer = 0; rightPointer < nums.size(); rightPointer++){
            tempValue += nums[rightPointer];
            while(tempValue > goal){
                tempValue -= nums[leftPointer];
                leftPointer++;
            }
            subarrayCount += (rightPointer - leftPointer + 1);
        }
        return subarrayCount;
    }
};