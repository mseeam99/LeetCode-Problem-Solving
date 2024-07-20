class MyStack {
public:
    MyStack() {}
    ~MyStack() {}

    queue<int> myQueueFinal;
    queue<int> myQueueTemp;
    
    void push(int x) {
        myQueueFinal.push(x);
    }
    
    int pop() {
        if (myQueueFinal.empty()) {
            throw std::runtime_error("Stack is empty");
        }
        
        while (myQueueFinal.size() > 1) {
            int tempValue = myQueueFinal.front();
            myQueueTemp.push(tempValue);
            myQueueFinal.pop();
        }
        
        int poppedValue = myQueueFinal.front();
        myQueueFinal.pop();
        
        swap(myQueueFinal, myQueueTemp);
        return poppedValue;
    }

    
    int top() {
        int value = myQueueFinal.back();
        return value;
    }
    
    bool empty() {
        bool answer = false;
        if(myQueueFinal.size() == 0){
            answer = true;
        }
        return answer; 
    }
};
