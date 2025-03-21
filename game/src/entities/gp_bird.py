from random import random
from entities.bird import Bird
from typing import List
from tools.bird_stats import BirdStats
from entities.DecisionTreeNode import DecisionTreeNode, FUNCTION_SET

TERMINAL_SET = {
        'B_pos_x': super.position.x,
        'B_pos_y': super.position.y,
        'P_pos_x': ...,
        'P_pos_y': ...
}

class GPBird(Bird):
    def __init__(self, hitbox, image, position, decision_tree: List = None):
        super().__init__(hitbox, image, position)
        self.__decision_tree = __generate_decision_tree(3)
        self.stats = BirdStats()


    def get_decision_tree(self):
        return self.__decision_tree

    def __generate_decision_tree(self, depth: int):
        if depth == 0:
            return DecisionTreeNode(random.choice(TERMINAL_SET.keys()))
        function = random.choice(FUNCTION_SET.keys())
        return DecisionTreeNode(function, self.__generate_decision_tree(depth - 1), self.__generate_decision_tree(depth - 1))


    
