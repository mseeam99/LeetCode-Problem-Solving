static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* actualHead = head;
        int totalLength = 0;

        while (head != NULL){
            totalLength++;
            head = head->next;
        }head = actualHead;

        if (totalLength == 1){return NULL;}

        int toDelete = totalLength - n + 1;
        int count = 1;
        if (toDelete == 1){return actualHead->next;}

        while(head!=NULL){
            if(count == toDelete - 1){
                head->next = head->next->next;
                break; 
            }
            head = head->next;
            count++;
        }head = actualHead;

        return actualHead;
    }
};