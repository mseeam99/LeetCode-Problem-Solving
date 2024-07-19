static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();


class Solution {
public:
    bool isValid(string s) {

        bool answer = false;

        vector <char> myVector;

        for(int i=0;i<s.size();i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                myVector.push_back(s[i]);
            }

            if(s[i] == ')'){
                if(myVector.size()!= 0 && myVector[myVector.size()-1] == '('){
                    myVector.pop_back();
                }else{
                    myVector.push_back(s[i]);
                }
            }

            if(s[i] == '}'){
                if(myVector.size()!= 0 && myVector[myVector.size()-1] == '{'){
                    myVector.pop_back();
                }else{
                    myVector.push_back(s[i]);
                }
            }

            if(s[i] == ']'){
                if(myVector.size()!= 0 && myVector[myVector.size()-1] == '['){
                    myVector.pop_back();
                }else{
                    myVector.push_back(s[i]);
                }
            }
        }

        if(myVector.size() == 0){
            answer = true;
        }

        return answer;

    }
};