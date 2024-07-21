static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {

        stack<int> myStack;
        int popPointer = 0;

        for(int i=0; i<pushed.size(); i++){
            myStack.push(pushed[i]);
            while(myStack.size()>0 && myStack.top() == popped[popPointer]){
                myStack.pop();
                popPointer++;
            }
        }

        bool answer = false;
        if(myStack.size()==0){
            answer = true;
        }

        return answer;

    }
};
