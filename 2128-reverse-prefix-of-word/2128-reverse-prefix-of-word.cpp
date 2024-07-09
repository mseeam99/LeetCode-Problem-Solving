static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    string reversePrefix(string word, char ch) {

        if(word.find(ch) == string::npos){
            return word;
        }

        string reversedString = "";
        int pointer = 0;

        while (pointer < word.size()){
            if (word[pointer] != ch){
                reversedString+=word[pointer];
                pointer++;
            }else if (word[pointer] == ch){
                reversedString+=word[pointer];
                break;
            }
        }

        pointer++;

        reverse(reversedString.begin(),reversedString.end());

        while (pointer < word.size()){
            reversedString+=word[pointer];
            pointer++;
        }

        return reversedString;
    }
};