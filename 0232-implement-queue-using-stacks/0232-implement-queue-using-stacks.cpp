# include <stack>

class MyQueue {
public:

    MyQueue() {}
    ~MyQueue() {}

    stack <int> myStackFinal;
    stack <int> myStackTemp;

    void push(int x) {
        myStackFinal.push(x);
    }
    
    int pop() {
        int tempTopValue = 0;

        while(myStackFinal.size() > 1){
            tempTopValue = myStackFinal.top();
            myStackTemp.push(tempTopValue);
            myStackFinal.pop();
        }

        tempTopValue = myStackFinal.top();
        myStackFinal.pop();

        while(myStackTemp.size() != 0){
            int newTempTopValue = myStackTemp.top();
            myStackFinal.push(newTempTopValue);
            myStackTemp.pop();
        }
        return tempTopValue;
    }
    
    int peek() {
        while(myStackFinal.size() > 1){
            int tempTopValue = myStackFinal.top();
            myStackTemp.push(tempTopValue);
            myStackFinal.pop();
        }

        int frontValue = myStackFinal.top();

        while(myStackTemp.size() != 0){
            int tempTopValue = myStackTemp.top();
            myStackFinal.push(tempTopValue);
            myStackTemp.pop();
        }
        return frontValue;
    }
    
    bool empty() {
        if(myStackFinal.size() == 0){
            return true;
        }else{
            return false;
        }
    }

};