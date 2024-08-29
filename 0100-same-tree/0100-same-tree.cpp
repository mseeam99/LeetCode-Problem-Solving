class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return traverse(p,q);
    }

    bool traverse(TreeNode* p, TreeNode* q){
        if(p == nullptr && q == nullptr) return true;
        if(p == nullptr || q == nullptr) return false;
        if(p->val != q->val)             return false;
        return traverse(p->left,q->left) && traverse(p->right,q->right);  
    }
};