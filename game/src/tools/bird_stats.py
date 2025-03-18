class BirdStats:
    def __init__(self):
        self.__score = -1
        self.__fitness = -1
    
    def set_score(self, score: int):
        self.__score = score
    
    def set_fitness(self, fitness: int):
        self.__fitness = fitness

    def get_score(self):
        return self.__score
    
    def get_fitness(self):
        return self.__fitness

    def __dict__(self):
        return {
            'score': self.score
        }