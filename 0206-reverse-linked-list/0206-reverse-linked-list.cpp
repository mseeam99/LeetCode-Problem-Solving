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

static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* tempHead = head;
        vector<int> variableStore;
        while(tempHead != nullptr){
            variableStore.push_back(tempHead->val);
            tempHead = tempHead->next;
        }
        tempHead = head;
        int index = 0;
        reverse(variableStore.begin(),variableStore.end());
        while(tempHead != nullptr){
            tempHead->val = variableStore.at(index);
            index++;
            tempHead = tempHead->next;
        }
        tempHead = head;
        return tempHead;
    }
};



