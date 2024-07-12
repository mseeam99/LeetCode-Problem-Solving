static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {

        vector<int> newVector;

        for (int i = 0; i < operations.size(); i++) {
            if (operations[i] == "+" && newVector.size() >= 2)  {
                int last = newVector[newVector.size() - 1];
                int leftLast = newVector[newVector.size() - 2];
                int tempSum = last + leftLast;
                newVector.push_back(tempSum);
            }else if (operations[i] == "D" && !newVector.empty()) {
                int tempValue = newVector[newVector.size() - 1];
                tempValue = tempValue * 2;
                newVector.push_back(tempValue);
            }else if (operations[i] == "C" && !newVector.empty()) {
                newVector.pop_back();
            }else {
                newVector.push_back(stoi(operations[i]));
            }
        }
        int answer = accumulate(newVector.begin(), newVector.end(), 0);
        return answer;
    }
};



