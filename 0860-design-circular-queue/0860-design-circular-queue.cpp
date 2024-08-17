class MyCircularQueue {
public:

    int capacity = 0;

    MyCircularQueue(int k) {
        capacity = k;
    }
    
    deque <int> myDeque;
    
    bool enQueue(int value) {
        if(myDeque.size() == capacity){
            return false;
        }
        myDeque.push_back(value);  
        return true;
    }
    
    bool deQueue() {
        if(myDeque.empty()) {
            return false;
        }
        myDeque.pop_front();  
        return true;
    }
    
    int Front() {
        if(myDeque.empty()){
            return -1;
        }
        return myDeque.front();
    }
    
    int Rear() {
        if(myDeque.empty()){
            return -1;
        }
        return myDeque.back();
    }
    
    bool isEmpty() {
        return myDeque.empty();
    }
    
    bool isFull() {
        return myDeque.size() == capacity;
    }
};