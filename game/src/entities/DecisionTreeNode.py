#from entities.gp_bird import TERMINAL_SET
import operator
import random

FUNCTION_SET = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda x, y: x / y if y != 0 else 1,

    'and': lambda x, y: x and y,
    'or': lambda x, y: x or y,
    #'not': operator.not_,

    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne
}

TERMINAL_SET = ['B_pos_x', 'B_pos_y', 'P_pos_x', 'P_pos_y']

class DecisionTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

def tree_to_expression(node: DecisionTreeNode):
    if node.is_leaf():
        return str(node.value)

    left_expr = tree_to_expression(node.left)
    right_expr = tree_to_expression(node.right)
    return f'({left_expr} {node.value} {right_expr})'



def get_random_node(node: DecisionTreeNode):
    if node.is_leaf():
        return node
    nodes = take_all_nodes(node)
    return random.choice(nodes)

def generate_random_tree():
    if random.random() < 0.5:
        return DecisionTreeNode(random.choice(TERMINAL_SET))
    function = random.choice(list(FUNCTION_SET.keys()))
    return DecisionTreeNode(function, generate_random_tree(),
                            generate_random_tree())

def take_all_nodes(node: DecisionTreeNode):
    if node.is_leaf():
        return [node]
    return [node] + take_all_nodes(node.left) + take_all_nodes(node.right)

def replace_node(tree: DecisionTreeNode, old_node: DecisionTreeNode, new_node: DecisionTreeNode):
    if tree.left is old_node:
        tree.left = new_node
    elif tree.right is old_node:
        tree.right = new_node
    else:
        replace_node(tree.left, old_node, new_node)
        replace_node(tree.right, old_node, new_node)






