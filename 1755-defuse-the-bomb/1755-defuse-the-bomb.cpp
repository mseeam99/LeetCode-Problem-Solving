static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {

        int actualSize = code.size();

        if(k == 0){
            for(int i=0; i<code.size(); i++){
                code.at(i) = 0;
            }return code;
        }

        if(k>0){
            vector<int> newVector;
            for(int i=0; i<code.size(); i++){
                newVector.push_back(code[i]);
            }
            for(int i=0; i<code.size(); i++){
                newVector.push_back(code[i]);
            }
            for(int i=0; i<code.size(); i++){
                int tempSum = accumulate(newVector.begin()+i+1,newVector.begin()+i+k+1,0);
                code[i] = tempSum;
            }
            return code;       
        }

        if(k<0){
            vector<int> newVector;
            int index = 0;
            for(int i=0; i<code.size(); i++){
                newVector.push_back(code[i]);
            }
            for(int i=0; i<code.size(); i++){
                newVector.push_back(code[i]);
            }
            for(int i=actualSize; i<newVector.size(); i++){
                int tempSum = accumulate(newVector.begin()+i+k,newVector.begin()+i,0);
                code[index++] = tempSum;
            }
            return code;       
        }
        return code;
    }
};