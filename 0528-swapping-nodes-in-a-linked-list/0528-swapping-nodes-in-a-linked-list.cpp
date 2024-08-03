/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
*/

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