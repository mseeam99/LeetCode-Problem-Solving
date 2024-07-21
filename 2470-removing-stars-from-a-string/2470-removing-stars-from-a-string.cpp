static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    string removeStars(string s) {
        string answer = "";
        for(int i=0; i<s.size(); i++){
            if(s[i] == '*' && answer.size()>0){
                answer.pop_back();
            }else{
                answer+=s[i];
            }
        }
        return answer;
    }
};