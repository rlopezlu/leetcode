class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def in_order(t1, t2):
        #break condition
            if(t1 is None and t2 is None):
                return None
            if(t1 is None):
                return t2
            if(t2 is None):
                return t1

            #current node
            t1.val = t1.val + t2.val
            #handle right side
            t1.right = in_order(t1.right, t2.right)
            #handle left side
            t1.left = in_order(t1.left, t2.left)
            return t1


        return in_order(t1, t2)
        
