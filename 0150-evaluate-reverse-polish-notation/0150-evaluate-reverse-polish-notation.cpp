static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

#include <stack>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        if(tokens.size()==1){
            return stoi(tokens[0]);
        }

        stack<int> myStack;

        for(int i=0; i<tokens.size(); i++){
            if(tokens[i] == "+"){
                int last = myStack.top();
                myStack.pop();
                int first = myStack.top();
                myStack.pop();
                int value = first + last;
                myStack.push(value);
            }
            else if(tokens[i] == "-"){
                int last = myStack.top();
                myStack.pop();
                int first = myStack.top();
                myStack.pop();
                int value = first - last;
                myStack.push(value);
            }
            else if(tokens[i] == "*"){
                int last = myStack.top();
                myStack.pop();
                int first = myStack.top();
                myStack.pop();
                int value = first * last;
                myStack.push(value);
            }
            else if(tokens[i] == "/"){
                int last = myStack.top();
                myStack.pop();
                int first = myStack.top();
                myStack.pop();
                int value = first / last;
                myStack.push(value);
            }
            else{
                int value = stoi(tokens[i]);
                myStack.push(value);
            }
        }
        return myStack.top();
    }
};