#include <iostream>
#include <vector>

static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        sort(nums.begin(),nums.end());

        int leftPointer  = 0;
        int rightPointer = nums.size()-1;
        float answer = ceil(1000000000000000.500);
        float currentValue = 0;
       
        while(leftPointer < rightPointer){
            currentValue = ceil(nums[leftPointer] + nums[rightPointer]) / 2;
            answer = min(answer,currentValue);
            leftPointer++;
            rightPointer--;
        }
        return answer;
    }
};