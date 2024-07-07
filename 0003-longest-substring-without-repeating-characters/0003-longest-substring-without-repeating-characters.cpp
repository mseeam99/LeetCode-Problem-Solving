#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_set<int> mySet; 

        int maxLength    = 0;
        int leftPointer  = 0;
        int rightPointer = 0;

        while(rightPointer < s.size()){
            if(mySet.find(s[rightPointer]) != mySet.end()){
                mySet.erase(s[leftPointer]);
                leftPointer++;
            }else if(mySet.find(s[rightPointer]) == mySet.end()){
                mySet.insert(s[rightPointer]);
                maxLength = max(maxLength,rightPointer-leftPointer+1);
                rightPointer++;   
            }
        }
        return maxLength;
    }
};
