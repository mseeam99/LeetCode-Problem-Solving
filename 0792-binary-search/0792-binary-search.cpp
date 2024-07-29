static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();


class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==1 && nums[0] != target) {
            return -1;
        }
        return answer(nums, 0, nums.size(), target);
    }

    int answer(vector<int>& nums, int left, int right, int target){
        while(left<=right){
            int middle = left + (right-left) / 2;
            if(nums[middle] == target){
                return middle;
            }
            else if(nums[middle] < target){
                left = middle + 1;
            }
            else if(nums[middle] > target){
                right = middle - 1;
            }
        }
        return -1;
    }
};