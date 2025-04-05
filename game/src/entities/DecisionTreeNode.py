#from entities.gp_bird import TERMINAL_SET
import operator
import random
from settings import JUMP_VELOCITY, FALL_ACCELERATION, BIRD_FALL_VELOCITY, PIPE_VELOCITY, PIPES_HORIZONTAL_GAP, PIPE_WIDTH, PIPES_VERTICAL_GAP
#from entities.gp_bird import SETTING_SET
SETTING_SET = {
    'jumpVel': JUMP_VELOCITY,
    'fallAccel': FALL_ACCELERATION,
    'birdFallVel': BIRD_FALL_VELOCITY,
    'pipeVel': PIPE_VELOCITY,
    'pipeHorGap': PIPES_HORIZONTAL_GAP,
    'pipeWidth': PIPE_WIDTH,
    'pipeVertGap': PIPES_VERTICAL_GAP
}
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
    def __init__(self, value, left=None, right=None, depth=1):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth

    def is_leaf(self):
        return self.left is None and self.right is None
    def get_tree_depth(self) -> int:
        if self is None:
            return 0
        if self.is_leaf():
            return 1
        return 1 + max(self.left.get_tree_depth(), self.right.get_tree_depth())



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

def generate_random_tree(depth: int = 0):
    if random.random() < 0.5 + 0.1 * depth:
        options = TERMINAL_SET + [str(random.randint(0, 99))] + list(SETTING_SET.keys())
        return DecisionTreeNode(random.choice(options))
    function = random.choice(list(FUNCTION_SET.keys()))
    return DecisionTreeNode(function, generate_random_tree(depth + 1),
                            generate_random_tree(depth + 1))

def take_all_nodes(root: DecisionTreeNode) -> list[DecisionTreeNode]:
    if root is None:
        return []
    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes
    # if node.is_leaf():
    #     return [node]
    # if node.left is None and node.right is None:
    #     return [node]
    # return [node] + take_all_nodes(node.left) + take_all_nodes(node.right)

def replace_node(tree: DecisionTreeNode, old_node: DecisionTreeNode, new_node: DecisionTreeNode):
    if tree is None:
        return None
    if tree is old_node:
        return new_node
    if tree.is_leaf():
        return tree

    new_left = replace_node(tree.left, old_node, new_node)
    new_right = replace_node(tree.right, old_node, new_node)

    if new_left is not tree.left or new_right is not tree.right:
        new_tree = DecisionTreeNode(tree.value, new_left, new_right)
        return new_tree

    return tree






