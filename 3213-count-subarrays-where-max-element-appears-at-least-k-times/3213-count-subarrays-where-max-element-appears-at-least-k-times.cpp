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

        int maxValue = *max_element(nums.begin(),nums.end());
        long long answer = 0;

        int count = 0;
        int leftPointer = 0;

        for(int rightPointer = 0; rightPointer<nums.size(); rightPointer++){

            if(nums[rightPointer] == maxValue){
                count++;
            }

            while(count >= k){
                answer += nums.size() - rightPointer; 
                if(nums[leftPointer] == maxValue){
                    count--;
                }
                leftPointer++;
            }

        }

        return answer;
        
    }
};