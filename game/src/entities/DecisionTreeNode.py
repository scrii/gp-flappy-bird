from entities.gp_bird import TERMINAL_SET
import operator

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




