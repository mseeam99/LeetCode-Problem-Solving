static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        vector<int> answer(temperatures.size(),0);
        stack<int> indexStack;

        for(int i=0; i<temperatures.size(); i++){
            while(!indexStack.empty() && temperatures[indexStack.top()] < temperatures[i]){
                answer[indexStack.top()] = i - indexStack.top();
                indexStack.pop();
            }
            indexStack.push(i);
        }
        return answer;
    }
};

