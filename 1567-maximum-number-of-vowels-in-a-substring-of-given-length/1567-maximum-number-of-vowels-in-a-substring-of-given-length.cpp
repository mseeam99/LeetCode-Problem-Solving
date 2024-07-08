static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int maxVowels(string s, int k) {

        int maxVowel = 0;
        int windowVowel = 0;

        unordered_set<char> myHashMap = {'a','e','i','o','u'};

        for(int i=0; i<k; i++){
            if(myHashMap.find(s[i]) != myHashMap.end()){
                windowVowel++;
            }
        }

        maxVowel = windowVowel;

        for(int i=k; i<s.size();i++){
            if(myHashMap.find(s[i-k]) != myHashMap.end()){
                windowVowel--;  
            }
            
            if(myHashMap.find(s[i]) != myHashMap.end()){
                windowVowel++;  
            }
            maxVowel = max(maxVowel,windowVowel);
        }
        return maxVowel ;
    }
};