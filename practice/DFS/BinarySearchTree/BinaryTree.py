class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
    
class BinaryTree:

    def __init__(self):
        self.root=None

    def insert(self,data):
        current_node=self.root
        if current_node==None:
            self.root=Node(data)
        else:
            if data<self.root.value:
                if self.root.left is None:
                    self.root.left=Node(data)
                else:
                    self.root.left.insert(data)
            else:
                if self.root.right is None:
                    self.root.right=Node(data)
                else:
                    self.root.right.insert(data)
                    

    def preOrder(self):
        self._preOrder(self.root)
    def _preOrder(self,root):
        
        if root==None:
            return
        print(root.value)
        self._preOrder(root.left)
        self._preOrder(root.right)

    def postOrder(self):
        self._postOrder(self.root)
    def _postOrder(self,root):
        if root==None:
            return
        self._preOrder(root.left)
        self._preOrder(root.right)
        print(root.value)

    def inOrder(self):
        self._inOrder(self.root)
    def _inOrder(self,root):
        if root==None:
            return
        self._preOrder(root.left)
        print(root.value)
        self._preOrder(root.right)

        
    def __str__(self):
        return(str(self.root.value))

            


def main():
    bt=BinaryTree()
    bt.insert(2)
    bt.insert(1)
    bt.insert(3)
    # bt.preOrder()
    # bt.postOrder()
    bt.inOrder()
if __name__ == "__main__":
    main()