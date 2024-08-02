class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> values;

        while (head!=NULL){
            values.push_back(head->val);
            head = head->next;
        }

        int leftPointer = 0;
        int rightPointer = values.size()-1;
        int maxValue = 0;
        int currentSum = 0;

        while(leftPointer < rightPointer){
            currentSum = values[leftPointer] + values[rightPointer];
            if (currentSum >= maxValue){maxValue = currentSum;}
            leftPointer++;
            rightPointer--;
        }

        return maxValue;
    }
};