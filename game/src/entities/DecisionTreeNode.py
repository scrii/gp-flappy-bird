from entities.gp_bird import TERMINAL_SET
import operator
import random

FUNCTION_SET = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda x, y: x / y if y != 0 else 1
}

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

def evalaute_tree(node: DecisionTreeNode):
    if node.is_leaf():
        return TERMINAL_SET[node.value]
    left_expr = evalaute_tree(node.left)
    right_expr = evalaute_tree(node.right)
    return FUNCTION_SET[node.value](left_expr, right_expr)

def get_random_node(node: DecisionTreeNode):
    if node.is_leaf():
        return node
    nodes = take_all_nodes(node)
    return random.choice(nodes)

def generate_random_tree():
    if random.random() < 0.5:
        return DecisionTreeNode(random.choice(TERMINAL_SET.keys()))
    function = random.choice(FUNCTION_SET.keys())
    return DecisionTreeNode(function, generate_random_tree(),
                            generate_random_tree())


def take_all_nodes(node: DecisionTreeNode):
    if node.is_leaf():
        return [node]
    return [node] + take_all_nodes(node.left) + take_all_nodes(node.right)

def replace_node(tree: DecisionTreeNode, old_node: DecisionTreeNode, new_node: DecisionTreeNode):
    # if tree.is_leaf():
    #     raise Exception("Tree is empty")
    if tree.left is old_node:
        tree.left = new_node
    elif tree.right is old_node:
        tree.right = new_node
    else:
        replace_node(tree.left, old_node, new_node)
        replace_node(tree.right, old_node, new_node)






