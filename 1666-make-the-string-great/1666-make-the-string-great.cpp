static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    string makeGood(string s) {

        string answer = "";

        for (int i=0; i<s.size(); i++) {
            if (!answer.empty() && abs(answer[answer.size()-1] - s[i]) == 32) {
                answer.pop_back();
            } else {
                answer += s[i];
            }
        }

        return answer;

    }
};
