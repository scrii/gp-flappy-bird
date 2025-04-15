from random import random, randint
import random
from unittest.mock import right

from entities.Bird import Bird
from typing import List

from pygments.lexers.robotframework import SETTING
from tools.bird_stats import BirdStats
from entities.DecisionTreeNode import DecisionTreeNode, FUNCTION_SET
from settings import JUMP_VELOCITY, FALL_ACCELERATION, BIRD_FALL_VELOCITY, PIPE_VELOCITY, PIPES_HORIZONTAL_GAP, PIPE_WIDTH, PIPES_VERTICAL_GAP


TERMINAL_SET = ['B_pos_x', 'B_pos_y', 'P_pos_x', 'P_pos_y']
SETTING_SET = {
    'jumpVel': JUMP_VELOCITY,
    'fallAccel': FALL_ACCELERATION,
    'birdFallVel': BIRD_FALL_VELOCITY,
    'pipeVel': PIPE_VELOCITY,
    'pipeHorGap': PIPES_HORIZONTAL_GAP,
    'pipeWidth': PIPE_WIDTH,
    'pipeVertGap': PIPES_VERTICAL_GAP
}
#TERMINAL_SET = ['B_pos_y', 'P_pos_x', 'P_pos_y', 'birdFallVel', 'pipeVel', ]

class GPBird(Bird):
    def __init__(self, hitbox, image, position, decision_tree: DecisionTreeNode = None):
        super().__init__(hitbox, image, position)
        self.init_depth = 5
        if (decision_tree is None):
            self.__decision_tree = self.__generate_decision_tree(self.init_depth)
        else:
            self.__decision_tree = decision_tree #__generate_decision_tree(3)
        self.stats = BirdStats()
        self.fitness = 0
        self.lifeTime = 0

    def make_decision(self, terminal_set):
        decision_tree = self.__decision_tree
        return evaluate_tree(decision_tree, terminal_set) % 2

    def get_decision_tree(self):
        return self.__decision_tree

    def __generate_decision_tree(self, depth: int):
        if depth == self.init_depth:
            function = random.choice(list(FUNCTION_SET.keys())[4:])
            left = self.__generate_decision_tree(depth - 1)
            right = self.__generate_decision_tree(depth - 1)
            return DecisionTreeNode(function, left, right)
        if depth == 0:
            options = (TERMINAL_SET +
                       [str(randint(0, 10))] +
                       list(SETTING_SET.keys()))
            return DecisionTreeNode(random.choice(options))
        function = random.choice(list(FUNCTION_SET.keys()))
        left = self.__generate_decision_tree(depth - 1)
        right = self.__generate_decision_tree(depth - 1)
        return DecisionTreeNode(function, left, right)

def evaluate_tree(node: DecisionTreeNode, terminal_set):
    if node.is_leaf():
        for i in range(len(terminal_set)):
            if node.value == TERMINAL_SET[i]:
                return terminal_set[i]
        # for i in range(len(terminal_set)):
        if node.value in SETTING_SET:
            return SETTING_SET[node.value]
        return int(node.value)
        # return TERMINAL_SET[node.value]
    left_expr = evaluate_tree(node.left, terminal_set=terminal_set)
    right_expr = evaluate_tree(node.right, terminal_set=terminal_set)
    return FUNCTION_SET[node.value](left_expr, right_expr)
    
