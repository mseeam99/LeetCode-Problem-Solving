class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* actualHead = head;
        vector <int> values;
        int currentNodeIndex = 1;

        while(head != nullptr){
            if(currentNodeIndex >= left && currentNodeIndex <= right){
                values.push_back(head->val);
            }
            currentNodeIndex+=1;
            head = head->next;
        }head = actualHead;
        currentNodeIndex = 1;
        
        reverse(values.begin(),values.end());
        int indexOfVector = 0;

        while(head != nullptr){
            if(currentNodeIndex >= left && currentNodeIndex <= right){
                head->val = values.at(indexOfVector++);
            }
            currentNodeIndex+=1;
            head = head->next;
        }head = actualHead;

        return head;
    }
};