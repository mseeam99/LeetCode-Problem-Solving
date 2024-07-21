static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class MinStack {
public:

    vector <int> stack;

    MinStack() {}

    void push(int val) {
        stack.push_back(val);
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return stack[stack.size()-1];
        
    }
    
    int getMin() {
        int minimumValue = *min_element(stack.begin(),stack.end());
        return minimumValue;
    }
};
