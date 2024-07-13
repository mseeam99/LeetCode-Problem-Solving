#define fast ios::sync_with_stdio(0),cin.tie(0),cout.tie(0)

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map <int,int> map;
        int rightPointer = 0;
        int leftPointer  = 0;
        int maxLength    = 0;
        for(rightPointer = 0; rightPointer < fruits.size(); rightPointer++){
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