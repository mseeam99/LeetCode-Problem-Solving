#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int init = [] {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    std::ofstream out("user.out");
    for (string str; getline(std::cin, str); out << "\n") {
        if (str.size() <= 2) {
            out << 0;
            continue;
        }
        int lastSeenPos[256] = {0};
        int res = 1;
        int l = 1;
        int r = 1;
        while (r < str.size() - 1) {
            if (lastSeenPos[str[r]] >= l) {
                res = max(res, r - l);
                l = lastSeenPos[str[r]] + 1;
            }
            lastSeenPos[str[r]] = r;
            ++r;
        }
        res = max(res, r - l);
        out << res;
    }
    out.flush();
    exit(0);
    return 0;
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
