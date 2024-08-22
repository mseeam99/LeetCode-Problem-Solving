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

    int maxDepth(TreeNode* root) {
        return returnDepth(root);
    }

    int returnDepth(TreeNode* recievedRoot){
        if(recievedRoot == nullptr) return 0;
        int leftSideDepth  = returnDepth(recievedRoot->left);
        int rightSideDepth = returnDepth(recievedRoot->right);
        return max(leftSideDepth,rightSideDepth) + 1; // +1 for root node
    }
};