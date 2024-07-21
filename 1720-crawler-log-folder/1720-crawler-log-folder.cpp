static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int minOperations(vector<string>& logs) {

        vector<string> tempVector;

        for(int i=0; i<logs.size(); i++){
            if(tempVector.size()!=0 && logs[i] == "../"){
                tempVector.pop_back();
            }else if(tempVector.size()==0 && logs[i] == "../"){
                continue;
            }else if(logs[i] == "./"){
                continue;
            }else{
                tempVector.push_back(logs[i]);
            }
        }
        return tempVector.size();
    }
};