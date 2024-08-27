class Solution {
public:
    bool checkTree(TreeNode* root) {
        
        bool answer = false;

        int firstValue = root->val;
        int leftValue = root->left->val;
        int rightValue = root->right->val;

        if(leftValue+rightValue == firstValue){
            answer = true;
        }

        return answer;
        
    }
};