static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> answer; 
        for (int i = 0; i < asteroids.size(); ++i) {
            if (asteroids[i] > 0) {
                answer.push_back(asteroids[i]);
            } else { 
                while (!answer.empty() && answer.back() > 0 && answer.back() < abs(asteroids[i])) {
                    answer.pop_back();
                }
                if (answer.empty() || answer.back() < 0) {
                    answer.push_back(asteroids[i]); 
                } else if (answer.back() == -asteroids[i]) {
                    answer.pop_back(); 
                }
            }
        }
        return answer;
    }
};


