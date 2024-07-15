static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {

        int leftPointer = 0;
        int maxLength = 0;

        for(int rightPointer = 0; rightPointer<s.size(); rightPointer++){

            int tempDifference = abs(int(s[rightPointer]) - int(t[rightPointer]));
            maxCost -= tempDifference;

            while(maxCost < 0 && leftPointer <= rightPointer){
                maxCost += abs(int(s[leftPointer]) - int(t[leftPointer]));
                leftPointer++;
            }
            maxLength = max(maxLength,rightPointer - leftPointer + 1);
        }
        return maxLength;
    }
};

