static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {

        int leftPointer = 0;
        int maxLength = 0;

        unordered_map <int,int> map;

        for(int rightPointer = 0; rightPointer<nums.size(); rightPointer++){
            map[nums[rightPointer]]++;

            while(map[nums[rightPointer]] > k){
                map[nums[leftPointer]]--;
                leftPointer++;
            }

            maxLength = max(maxLength,rightPointer - leftPointer + 1);

        }
        return maxLength;
    }
};