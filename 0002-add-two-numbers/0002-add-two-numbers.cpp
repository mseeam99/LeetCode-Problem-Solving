static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* newNode = new ListNode();
        ListNode* trackNewNode = newNode;

        int carry = 0;

        while(l1 != nullptr || l2 != nullptr || carry != 0){

            int listOneValue = 0;
            int listTwoValue = 0;

            if(l1 != nullptr){
                listOneValue = l1->val;
                l1 = l1->next;
            }

            if(l2 != nullptr){
                listTwoValue = l2->val;
                l2 = l2->next;
            }

            int valueToAssign = listOneValue + listTwoValue + carry;
            carry = valueToAssign / 10;
            valueToAssign = valueToAssign % 10;

            ListNode* newNodeWithProperValue = new ListNode(valueToAssign);
            trackNewNode->next = newNodeWithProperValue;
            trackNewNode = trackNewNode->next;
        }

        ListNode* returnNode = newNode->next;
        delete newNode;
        return returnNode;
        
    }
};