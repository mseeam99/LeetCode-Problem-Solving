static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {

        if(head == nullptr || k == 0 || head->next == nullptr) return head;

        ListNode* actualHead      = head;
        ListNode* returnHead      = head;
        ListNode* actualHeadAgain = head;

        int totalLength = 0;
        
        while(head->next != nullptr){
            totalLength+=1;
            head = head->next;
        }totalLength+=1;
        head->next = actualHead;

        int reversedFromFirst = totalLength - (k % totalLength);

        for (int i=0; i<reversedFromFirst; i++){
            if(i == reversedFromFirst-1){
                returnHead = actualHeadAgain->next;
                actualHeadAgain->next = nullptr;
                break;
            }
            actualHeadAgain = actualHeadAgain->next;
        }
        return returnHead;
    }
};

