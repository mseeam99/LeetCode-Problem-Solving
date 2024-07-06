static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map <int,int> myMap;
        for(int i=0;i<nums.size();i++){
            if(myMap.find(nums[i])!=myMap.end()){
                int tempJ = myMap[nums[i]];
                if ((i - tempJ) <= k) {
                    return true;
                }
            }
            myMap[nums[i]] = i;
        }
        return false;
    }
};