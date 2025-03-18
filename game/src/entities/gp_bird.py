from entities.bird import Bird
from typing import List
# from tools.bird_stats import BirdStats

class GPBird(Bird):
    def __init__(self, hitbox, image, position, decision_tree: List = None):
        super().__init__(hitbox, image, position)
        self.__decision_tree = decision_tree
        # self.stats = BirdStats()
    
    def __generate_decision_tree(self):
        # TODO
        pass

    
