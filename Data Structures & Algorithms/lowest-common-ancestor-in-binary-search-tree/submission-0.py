# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca (node,p,q):
            if node is None:
                return None
            if node == p or node ==q:
                return node
            left = lca(node.left,p,q)
            right = lca(node.right,p,q)
            if left and right:
                return node
            else:
                return left or right

        
        return lca(root,p,q)