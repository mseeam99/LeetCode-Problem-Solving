class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> answer;
        inorder(root,answer);
        return answer;
    }

    void inorder(TreeNode* rootRecieved, vector<int> &answer){
        if (rootRecieved == nullptr) return;
        inorder(rootRecieved->left,answer);
        answer.push_back(rootRecieved->val);
        inorder(rootRecieved->right,answer);
    }
};