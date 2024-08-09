class Solution {
public:
    bool hasCycle(ListNode *head) {

        bool answer = false;
        
        ListNode *slow = head;
        ListNode *fast = head;

        while(slow != nullptr && fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast){
                answer = true;
                break;
            }
        }
        return answer;
    }
};