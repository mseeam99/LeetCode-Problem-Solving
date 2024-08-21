static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

#include <cmath>

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {

        vector<ListNode*> finalAnswer;
        ListNode* actualHead = head;

        int totalNodes = 0;

        while(actualHead != nullptr){
            totalNodes+=1;
            actualHead = actualHead->next;
        }actualHead = head;

        if(totalNodes <= k){
            int itaration = 0;
            while(itaration < k){
                if(actualHead!=nullptr){
                    ListNode* newPointerOfList = new ListNode(actualHead->val);
                    actualHead = actualHead->next;
                    finalAnswer.push_back(newPointerOfList);
                }else if(actualHead==nullptr){
                    finalAnswer.push_back(nullptr);
                }   
                itaration++; 
            }
        }else{

            vector<int> elementsOfEachList;
            double totalList = 0.0;  
            double firstListElements = 0.0;
           
            while(totalNodes != 0){
                if(elementsOfEachList.size()==0){
                    totalList = k % totalNodes;  
                    firstListElements = ceil((static_cast<double>(totalNodes)) / (static_cast<double>(totalList)));
                    elementsOfEachList.push_back(static_cast<int>(firstListElements));
                    totalNodes-=firstListElements;
                    totalList--;
                }else{
                    firstListElements = ceil((static_cast<double>(totalNodes)) / (static_cast<double>(totalList)));
                    elementsOfEachList.push_back(static_cast<int>(firstListElements));
                    totalNodes-=firstListElements;
                    totalList--;
                }
            }

            bool firstDone = false;
            int index = 0;

            for(int i=0; i<elementsOfEachList.size(); i++){
                if (firstDone == false){
                    int tempIteration = 0;
                    ListNode* newPointerOfList = new ListNode();
                    ListNode* temp = newPointerOfList;
                    while(tempIteration < elementsOfEachList[index]){
                        temp->next = new ListNode(actualHead->val);
                        temp = temp->next;
                        actualHead = actualHead->next;
                        tempIteration++;
                    }index++;
                    firstDone = true;
                    finalAnswer.push_back(newPointerOfList->next);
                }else{
                    int tempIteration = 0;
                    ListNode* newPointerOfList = new ListNode();
                    ListNode* temp = newPointerOfList;
                    while(tempIteration < elementsOfEachList[index]){
                        temp->next = new ListNode(actualHead->val);
                        temp = temp->next;
                        actualHead = actualHead->next;
                        tempIteration++;
                    }index++;
                    finalAnswer.push_back(newPointerOfList->next);
                }
            }
        }
        return finalAnswer;
    }
};