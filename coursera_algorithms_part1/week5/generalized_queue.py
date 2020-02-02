class QueueNode:
    def __init__(self, key):
        self.left = self.right=None
        self.key = key
        self.isRed = True
        self.size = 1

    def __str__(self):
        return f'key={self.key}, isRed={self.isRed}, size=self.size'

    def __repr__(self):
        return f'key={self.key}, isRed={self.isRed}, size={self.size}'


class GeneralizedQueue:
    def __init__(self):
        self.root = None
    
    def append(self, node):
        self.root  = self.appendR(self.root, node)
        self.root.isRed = False

    def appendR(self, root, node):
        added = False
        if not root:
            return node
        else:
            root.right = self.appendR(root.right, node)
            root.size += 1

        if root.right and root.right.isRed:
            root = self.left_rotate(root)
        if root.left and root.left.isRed and root.left.left and root.left.left.isRed:
            root = self.right_rotate(root)
        if root.left and root.left.isRed and root.right and root.right.isRed:
            root = self.flip_colors(root)
        return root

    def remove_front(self):
        return self.remove_ith(1)



    def inorder(self, root, data=None):
        if root:
            self.inorder(root.left, data)
            data.append(root.key)
            self.inorder(root.right, data)
    
    def get_inorder_succ(self, root):
        while(root and root.left):
            root = root.left
        return root
    
    def get_size(self, node):
        if node:
            return node.size
        else:
            return 0   

    def get_ith(self, i):
        tmp = self.get_ithR(self.root, i)
        if tmp:
            return tmp.key
        else:
            return None

    def get_ithR(self, root, i):
        if self.get_size(root) < i:
            return None
        else:
            if self.get_size(root.left) >= i:
                return self.get_ithR(root.left, i)
            elif self.get_size(root.left) == i - 1:
                return root
            else:
                return self.get_ithR(root.right, i-self.get_size(root.left)-1)
    
    def remove_ith(self, i):
        key = self.get_ith(i)    
        self.root = self.remove_ithR(self.root, i)
        if self.root and self.root.isRed:
            self.root.isRed = False
        return key

    def remove_ithR(self, root, i):
        if self.get_size(root) < i:
            return None
        else:
            if self.get_size(root.left) >= i:
                root.left  = self.remove_ithR(root.left, i)
            elif self.get_size(root.left)+1 < i:
                root.right = self.remove_ithR(root.right, i-self.get_size(root.left)-1)
            else:
                if not root.right:
                    root = root.left
                else:
                    tmp = self.get_ithR(root.right, 1)
                    root.key = tmp.key
                    root.right = self.remove_ithR(root.right, 1)

            if root and root.right and root.right.isRed:
                root = self.left_rotate(root)
            if root and root.left and root.left.isRed and root.left.left and root.left.left.isRed:
                root = self.right_rotate(root)
            if root and root.left and root.left.isRed and root.right and root.right.isRed:
                root = self.flip_colors(root)
        return root

    def left_rotate(self, root):
        assert root.right
        assert root.right.isRed
        root.isRed, root.right.isRed = root.right.isRed, root.isRed
        tmp = root.right
        root.size = root.size - tmp.size + self.get_size(tmp.left)
        tmp.size =  1 + root.size + self.get_size(tmp.right) 
        root.right = tmp.left
        tmp.left = root
        return tmp

    def right_rotate(self, root):
        assert root.left.isRed
        assert root.left.left.isRed
        root.left.isRed, root.isRed = root.isRed, root.left.isRed
        tmp = root.left
        root.size = 1 + self.get_size(root.right) + self.get_size(root.left.right)
        tmp.size = 1 + self.get_size(root) + self.get_size(tmp.left)
        root.left = tmp.right
        tmp.right = root
        return tmp

    def flip_colors(self, root):
        assert root.left
        assert root.right
        assert root.left.isRed
        assert root.right.isRed
        root.left.isRed = root.left.isRed = False
        root.isRed = True
        return root


import unittest
import random
class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.size = 10
        self.items = list([random.randint(1,self.size*self.size) for x in range(self.size)])

    def test_append(self):
        gq = GeneralizedQueue()
        for each in self.items:
            gq.append(QueueNode(each))
        tmp = []
        gq.inorder(gq.root, tmp)
        assert tmp==self.items

    def test_remove_front(self):
        gq = GeneralizedQueue()
        for each in self.items:
            gq.append(QueueNode(each))
        assert self.items[0] == gq.remove_front()
        tmp = []
        gq.inorder(gq.root, tmp)
        assert tmp==self.items[1:]
        assert self.items[1] == gq.remove_front()
        tmp = []
        gq.inorder(gq.root, tmp)
        assert tmp==self.items[2:]

    def test_return_ith_item(self):
        gq = GeneralizedQueue()
        for each in self.items:
            gq.append(QueueNode(each))
        i = random.randint(1, len(self.items))
        assert gq.get_ith(i) == self.items[i-1]

    
    def test_remove_ith_item(self):
        gq = GeneralizedQueue()
        for each in self.items:
            gq.append(QueueNode(each))
        i = random.randint(1, len(self.items))
        assert self.items[i-1] == gq.remove_ith(i)
        tmp = []
        gq.inorder(gq.root, tmp)
        del self.items[i-1]
        assert tmp == self.items
    

if __name__ == '__main__':
    unittest.main()
