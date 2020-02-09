from abc import ABC, abstractmethod

class Strategy:
    def __init__(self):
        pass

    @abstractmethod
    def move(self, game, player_id):
        pass

    @abstractmethod
    def game_over(self, reward):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_name(self):
        pass