import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def is_BT_a_BST_R(root):
    isBst, mn, mx = True, None, None
    if root:
        mn = mx = root.key
        isBstL, mnL, mxL = is_BT_a_BST_R(root.left)
        if isBstL and (not mxL or mxL <= root.key):
            if mnL:
                mn = mnL
            isBstR, mnR, mxR = is_BT_a_BST_R(root.right)
            if isBstR and (not mnR or mnR >= root.key):
                if not mn and mnR:
                    mn = mnR
                if mxR:
                    mx = mnR
            else:
                isBst = False
        else:
            isBst = False
    return isBst, mn, mx


def is_BT_a_BST(root):
    isbst, _, _  = is_BT_a_BST_R(root)
    return isbst


class TestIsBTABST(unittest.TestCase):
    def setUp(self):
        t = None

    def test_BT(self):
        t = Node(50)
        self.assertEqual(True, is_BT_a_BST(t))
        t.left = Node(60)
        self.assertEqual(False, is_BT_a_BST(t))
        t.left = Node(40)
        t.right = Node(60)
        self.assertEqual(True, is_BT_a_BST(t))


if __name__ == '__main__':
    unittest.main()
