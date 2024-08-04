class Node {
public:
    int val;
    Node* next; 

    Node(int r_val){
        val = r_val; 
        next = nullptr;       
    }

    Node(int r_val, Node* r_next){
        val = r_val;
        next = r_next;
    }
};

class MyLinkedList {
public:

    Node *nodePointer;

    MyLinkedList() {
        nodePointer = nullptr;
    }
    
    int get(int index) {
        if(index < 0) return -1;
        int current = 0;
        Node *head = nodePointer;
        while(head != nullptr && current < index){
            head = head->next;
            current++;
        } 
        return (head != nullptr) ? head->val : -1;
    }
    
    void addAtHead(int val) {
        Node *newNode = new Node(val);
        newNode->next = nodePointer;
        nodePointer = newNode;
    }
    
    void addAtTail(int val) {
        Node *newNode = new Node(val);
        if (nodePointer == nullptr) {
            nodePointer = newNode;
        } else {
            Node *head = nodePointer;
            while (head->next != nullptr) {
                head = head->next;
            }
            head->next = newNode;
        }
    }
    
    void addAtIndex(int index, int val) {
        if(index <= 0 ){
            addAtHead(val);
        }else{
            int current = 0;
            Node *head = nodePointer;
            while(head != nullptr && current < index-1){
                head = head->next;
                current++;
            }
            if(head!=nullptr){
                Node *newNode = new Node(val);
                newNode->next = head->next;
                head->next = newNode;

            }
        }
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || nodePointer == nullptr) return;
        if (index == 0) {
            Node *temp = nodePointer;
            nodePointer = nodePointer->next;
            delete temp;
        } else {
            Node *head = nodePointer;
            int current = 0;
            while (head->next != nullptr && current < index - 1) {
                head = head->next;
                current++;
            }
            if (head->next != nullptr) {
                Node *temp = head->next;
                head->next = head->next->next;
                delete temp;
            }
        }
    }
};

