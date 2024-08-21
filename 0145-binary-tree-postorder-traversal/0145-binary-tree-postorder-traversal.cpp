/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
*/

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> answer;
        postOrder(root,answer);
        return answer;
    }

    void postOrder(TreeNode* recievedRoot, vector<int> &answer){
        if (recievedRoot == nullptr) return;
        postOrder(recievedRoot->left,answer);
        postOrder(recievedRoot->right,answer);
        answer.push_back(recievedRoot->val);
    }
};