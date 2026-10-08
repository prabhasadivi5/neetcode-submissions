class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}

        # preorder[pl:pr] and inorder[il:ir] describe the current subtree
        def recurse(pl, pr, il, ir):
            if pl >= pr:
                return None

            rootVal = preorder[pl]
            root = TreeNode(rootVal)
            leftsize = idx[rootVal] - il

            root.left = recurse(pl + 1, pl + 1 + leftsize, il, il + leftsize)
            root.right = recurse(pl + 1 + leftsize, pr, il + leftsize + 1, ir)
            return root

        return recurse(0, len(preorder), 0, len(inorder))