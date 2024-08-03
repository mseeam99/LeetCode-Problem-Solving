static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    Node* copyRandomList(Node* head) {

        unordered_map <Node*,Node*> myMap;

        Node* actualHead = head;

        while(head!=NULL){
            myMap[head] = new Node(head->val);
            head = head->next;
        } head = actualHead;

        while(head!=NULL){
            Node* &getTheNode = myMap[head];
            getTheNode->next = myMap[head->next];
            getTheNode->random = myMap[head->random];
            head = head->next;
        }   head = actualHead;

        return myMap[head];
    }
};