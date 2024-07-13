static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map <int,int> map;
        int leftPointer  = 0;
        int maxLength    = 0;
        for(int rightPointer = 0; rightPointer < fruits.size(); rightPointer++){
            map[fruits[rightPointer]]++;
            
            if(map.size()>2){
                while(map.size()>2){
                    map[fruits[leftPointer]]--;
                    if(map[fruits[leftPointer]] == 0){
                        map.erase(fruits[leftPointer]);
                    }
                    leftPointer++;
                }
            }

            maxLength = max(maxLength,rightPointer-leftPointer + 1);
        }
        return maxLength;     
    }
};