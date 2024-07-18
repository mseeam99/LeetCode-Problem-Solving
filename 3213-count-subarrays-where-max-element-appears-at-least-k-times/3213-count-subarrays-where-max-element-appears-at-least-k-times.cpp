static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {

        int maxElement = *max_element(nums.begin(), nums.end());
        int count = 0;
        long long result = 0;
        
        int left = 0;
        int right = 0;
        
        for(int right = 0; right < nums.size(); right++){
            if (nums[right] == maxElement) {
                count++;
            }


            while (count >= k) {
                result += nums.size() - right;
                if (nums[left] == maxElement) {
                    count--;
                }left++;
            }

            
        }
        
        return result;
    }
};
