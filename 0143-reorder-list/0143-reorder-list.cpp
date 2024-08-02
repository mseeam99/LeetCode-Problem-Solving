static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    void reorderList(ListNode* head) {

        vector<int> values;
        ListNode* actualHead = head;

        while(head != NULL){
            values.push_back(head->val);
            head = head->next;
        }head = actualHead;

        vector<int> reordered;
        int left = 0, right = values.size() - 1;
        while (left <= right) {
            if (left == right) {
                reordered.push_back(values[left]);
                break;
            }
            reordered.push_back(values[left++]);
            reordered.push_back(values[right--]);
        }

        int count = 0;
        while(head!=NULL){
            head->val = reordered[count++];
            head = head->next;
        }head = actualHead;
        
    }
};