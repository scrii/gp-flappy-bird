from random import random, randint
import random
from entities.Bird import Bird
from typing import List
from tools.bird_stats import BirdStats
from entities.DecisionTreeNode import DecisionTreeNode, FUNCTION_SET
from settings import JUMP_VELOCITY, FALL_ACCELERATION, BIRD_FALL_VELOCITY


TERMINAL_SET = ['B_pos_x', 'B_pos_y', 'P_pos_x', 'P_pos_y']
#TERMINAL_SET = ['B_pos_y', 'P_pos_x', 'P_pos_y', 'birdFallVel', 'pipeVel', ]

class GPBird(Bird):
    def __init__(self, hitbox, image, position, decision_tree: DecisionTreeNode = None):
        super().__init__(hitbox, image, position)
        if (decision_tree is None):
            self.__decision_tree = self.__generate_decision_tree(5)
        else:
            self.__decision_tree = decision_tree #__generate_decision_tree(3)
        self.stats = BirdStats()

    def make_decision(self, terminal_set):
        decision_tree = self.__decision_tree
        return evaluate_tree(decision_tree, terminal_set)

    def get_decision_tree(self):
        return self.__decision_tree

    def __generate_decision_tree(self, depth: int):
        if depth == 0:
            return DecisionTreeNode(random.choice(TERMINAL_SET + list(str(randint(0, 99)))))
        function = random.choice(list(FUNCTION_SET.keys()))
        return DecisionTreeNode(function, self.__generate_decision_tree(depth - 1), self.__generate_decision_tree(depth - 1))

def evaluate_tree(node: DecisionTreeNode, terminal_set):
    if node.is_leaf():
        for i in range(len(terminal_set)):
            if node.value == TERMINAL_SET[i]:
                return terminal_set[i]
        return int(node.value)
        # return TERMINAL_SET[node.value]
    left_expr = evaluate_tree(node.left, terminal_set=terminal_set)
    right_expr = evaluate_tree(node.right, terminal_set=terminal_set)
    return FUNCTION_SET[node.value](left_expr, right_expr)
    
