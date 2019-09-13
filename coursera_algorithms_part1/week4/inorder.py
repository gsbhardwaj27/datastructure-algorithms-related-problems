def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
