class Node:
    def __init__(self,data) -> None:
            self.data=data
            self.right=None
            self.left=None

class Tree:
        def createNode(self,data):
            return Node(data)
        def insert(self,node,data):
            if node is None:
                  return self.createNode(data)
            if data < node.data:
                  node.left=self.insert(node.left,data)
            else:
                  node.right=self.insert(node.right,data)

            return node
        def inorder_traversal(self,root):
              if root is not None:
                    self.inorder_traversal(root.left)
                    print(root.data, end=" ")
                    self.inorder_traversal(root.right)
                    
        def preorder_traversal(self,root):
              if root is not None:
                    print(root.data,end=" ")
                    self.preorder_traversal(root.left)
                    self.preorder_traversal(root.right)
                    

        def post_order(self,root):
              if root is not None:
                    self.post_order(root.left)
                    self.post_order(root.right)  
                    print(root.data,end=" ")   
                    
        def delete(self,root,node):
            if root is None:
                 return None
            if node<root.data:
                 root.left=self.delete(root.left,node)
            if node>root.data:
                  root.right=self.delete(root.right,node)

            else:
                  if (root.left is None) and (root.right is None):
                        return None
                  if (root.left is None) and (root.right is not None):
                        return root.right
                  if (root.left is not None) and (root.right is None):
                        return root.left
                  else:
                        pnt=root.right
                        while pnt.left:
                              pnt=pnt.left
                        root.val=pnt.val
                        root.right=self.delete(root.right,root.val)
                
tree=Tree()
root=tree.createNode(5)
tree.insert(root,6)
tree.insert(root,7)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,9)
tree.insert(root,2)
tree.insert(root,0)
tree.inorder_traversal(root)
print()
tree.preorder_traversal(root)
print()
tree.post_order(root)

