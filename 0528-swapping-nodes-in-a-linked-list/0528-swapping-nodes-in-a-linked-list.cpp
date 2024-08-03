static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {

        vector<int> values;

        ListNode* actualHead = head;

        while (head != NULL){
            values.push_back(head->val);
            head = head->next;
        }head = actualHead;

        swap(values[k-1],values[values.size()-k]);
        int count = 0;

        while (head != NULL){
            head->val = values[count++];
            head = head->next;
        }head = actualHead;

        return head;    
    }
};