# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:  
    
    def serialize(self, root):
        ans = ""
        if root == None:
            return ""
        
        def ntos(node):
            nonlocal ans
            val = node.val + 1024
            tmp = ""
            while val != 0:
                tmp = str(val%2) + tmp
                val = val//2
            
            if len(tmp) < 11:
                tmp = "0"*(11-len(tmp))+tmp          
            ans += tmp
            
            if node.left != None:
                ntos(node.left)
            else :
                ans += "00000000000"
                
            if node.right != None:
                ntos(node.right)
            else :
                ans += "00000000000"
        
        ntos(root)
        # print(ans)
        return ans
        
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if data == "":
            return []
        p = 0
        end = len(data)
        
        def ston(p):
            node = TreeNode()
            cnt = 10
            val = 0
            
            while 0<=cnt:
                if int(data[p]):
                    val += 2**cnt
                cnt -= 1
                p += 1

            if val == 0:
                return [None,p]
            
            node.val = val-1024
            node.left,p = ston(p)
            node.right,p = ston(p)
            
            return [node,p]
        
        ans = ston(0)[0]
        return ans
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))