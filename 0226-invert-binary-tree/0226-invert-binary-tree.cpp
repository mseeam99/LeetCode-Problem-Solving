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
    TreeNode* invertTree(TreeNode* root) {
        TreeNode* answer = root;
        preOrder(root);
        return answer;
    }

    void preOrder(TreeNode* root){
        if (root==nullptr) return;
        TreeNode* tempRoot = root->left;
        root->left = root->right;
        root->right = tempRoot;
        preOrder(root->left);
        preOrder(root->right);
    }
};