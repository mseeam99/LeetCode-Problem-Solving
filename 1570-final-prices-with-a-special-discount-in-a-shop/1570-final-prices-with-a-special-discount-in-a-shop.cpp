static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {

        vector<int> answer;
        int pointer;

        for(int i=0;i<prices.size();i++){
            pointer = i+1;
            while(pointer < prices.size()){
                if (prices[pointer] <= prices[i]){
                    answer.push_back(prices[i] - prices[pointer]);
                    break;
                }
                pointer++;
            }
            if(pointer == prices.size()){
                answer.push_back(prices[i]);
            }
        }
        return answer;

    }
};