static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int smallPointer = 0;
        int bigPointer = 0;
        while (smallPointer < s.size() && bigPointer < t.size()){
            if (s[smallPointer] == t[bigPointer]){
                smallPointer++;
                bigPointer++;
            }else{
                bigPointer++;
            }
        }
        if (smallPointer == s.size()){
            return true;
        }else{
            return false;
        }
    }
};