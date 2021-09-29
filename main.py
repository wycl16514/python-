import pdb


class Node:
    def __init__(self, key: str, priority: float):
        self._key = key
        self._priority = priority
        self._left: Node = None
        self._right: Node = None
        self._parent: Node = None

    @property
    def key(self):
        return self._key

    @property
    def priority(self):
        return self._priority

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node.parent = self

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node.parent = self

    @parent.setter
    def parent(self, node):
        self._parent = node

    def is_root(self) -> bool:
        if self.parent is None:
            return True
        return False

    def is_leaf(self)->bool:
        if self.left is None and self.right is None:
            return True
        return False

    def __repr__(self):
        return "({}, {})".format(self._key, self._priority)

    def __str__(self):
        repr_str: str = ""
        repr_str += repr(self)
        if self.parent is not None:
            repr_str += " parent: " + repr(self.parent)
        else:
            repr_str += " parent: None"

        if self.left is not None:
            repr_str += " left: " + repr(self.left)
        else:
            repr_str += " left: None"

        if self.right is not None:
            repr_str += " right: " + repr(self.right)
        else:
            repr_str += " right: None"

        return repr_str


class Treap:
    def __init__(self):
        self._root: Node = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def right_rotate(self, x: Node):
        if x is None or x.is_root() is True:
            return

        y = x.parent
        if y.left != x:  # 必须是左孩子才能右旋转
            return

        p = y.parent
        if p is not None:  # 执行右旋转
            if p.left == y:
                p.left = x
            else:
                p.right = x
        else:
            self._root = x

        y.left = x.right
        x.right = y

    def left_rotate(self, x : Node):
        if x is None or x.is_root() is True:
            return

        y = x.parent
        if y.right is not x: # 只有右孩子才能左旋转
            return

        p = y.parent
        if p is not None:
            if p.left is y:
                p.left = x
            else:
                p.right = x
        else:
            self._root = x

        y.right = x.left
        x.left = y

    def insert(self, key: str, priority: int):
        node: Node = self.root
        parent: Node = None
        new_node = Node(key, priority)

        pdb.set_trace()

        while node is not None:  # 先根据key进行二叉树插入
            parent = node
            if node.key > key:
                node = node.left
            else:
                node = node.right

        if parent is None:
            self.root = new_node
            return
        elif key <= parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

        while new_node.parent is not None and new_node.priority < new_node.parent.priority:
            # 持续判断是否违反小堆性质
            if new_node == new_node.parent.left:  # 如果是左孩子那么执行右旋转
                self.right_rotate(new_node)
            else:  # 如果是右孩子则进行左旋转
                self.left_rotate(new_node)

        if new_node.parent is None:
            self.root = new_node

    def search(self, key : str):
        node = self.root
        while node is not None:
            if node.key == key:
                return node
            if node.key < key:
                node = node.right
            else:
                node = node.left
        return None

    def remove(self, key):
        node = self.search(key)  #查找包含给定字符串的节点
        if node is None:
            return False

        if node.is_root() and node.is_leaf(): #如果只有一个节点那么将treap设置为空
            self.root = None
            return True

        while not node.is_leaf():#把当前节点优先级设置为无穷大,因此要把左右孩子中优先级较小的那个进行旋转
            if node.left is not None and (node.right is None or node.left.priority < node.right.priority):
                self.right_rotate(node.left)
            else:
                self.left_rotate(node.right)

            if node.parent.is_root():
                self.root = node.parent

        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

        return True

    def top(self):
        if self.root is None:
            return None

        key = self.root.key
        self.remove(key)
        return key

def setup_right_rotate():
    flour: Node = Node("Flour", 10)
    cabbage: Node = Node("Cabbage", 77)
    beer: Node = Node("Beer", 76)
    eggs: Node = Node("Eggs", 129)
    bacon: Node = Node("Bacon", 95)
    butter: Node = Node("Butter", 86)

    flour.parent = None
    flour.left = cabbage
    flour.right = None
    cabbage.left = beer
    cabbage.right = eggs

    beer.left = bacon
    beer.right = butter

    return flour, beer, cabbage




def print_treap(n: Node):
    if n is None:
        return

    print(n)
    print_treap(n.left)
    print_treap(n.right)



def setup_treap_insert():
    flour: Node = Node("Flour", 10)
    butter: Node = Node("Butter", 76)
    water: Node = Node("Water", 32)
    bacon: Node = Node("Bacon", 77)
    eggs: Node = Node("Eggs", 129)
    milk: Node = Node("Milk", 55)
    cabbage: Node = Node("Cabbage", 159)
    pork : Node = Node("Pork", 56)

    flour.left = butter
    flour.right = water

    butter.left = bacon
    butter.right = eggs

    water.left = milk

    eggs.left = cabbage

    milk.right = pork

    return flour
'''
root = setup_treap_insert()
treap = Treap()
treap.root = root
treap.insert("Beer", 20)
print_treap(root)
'''

def setup_treap_remove():
    flour: Node = Node("Flour", 10)
    beer: Node = Node("Beer", 20)
    butter: Node = Node("Butter", 76)
    water: Node = Node("Water", 32)
    eggs: Node = Node("Eggs", 129)
    milk: Node = Node("Milk", 55)
    cabbage: Node = Node("Cabbage", 159)
    pork: Node = Node("Pork", 56)
    beet : Node = Node("Beet", 81)

    flour.left = beer
    flour.right = water
    beer.right = butter
    water.left = milk

    butter.left = beet
    butter.right = eggs
    eggs.left = cabbage

    milk.right = pork

    return flour

root = setup_treap_remove()
treap = Treap()
treap.root = root
treap.remove("Butter")
print_treap(root)







