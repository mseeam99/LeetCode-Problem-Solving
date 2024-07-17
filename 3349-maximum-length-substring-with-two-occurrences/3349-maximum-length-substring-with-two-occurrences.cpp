class Solution {
public:
    int maximumLengthSubstring(string s) {
        unordered_map <char,int> map;
        int maxLength = 0;
        int leftPointer = 0;
        for(int rightPointer = 0; rightPointer < s.size(); rightPointer++){
            map[s[rightPointer]]++;
            while(map[s[rightPointer]] > 2){
                map[s[leftPointer]]--;
                leftPointer++;
            }
            maxLength = max(maxLength, rightPointer-leftPointer+1);
        }
        return maxLength;
    }
};