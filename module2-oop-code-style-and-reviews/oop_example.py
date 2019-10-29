"""""""""
Classes to represent games
"""""""""
from random import random


class Game:
    """
    below are variables defined inside of a class
    """
    fun_level = 5 

    def __init__(self,rounds = 2,player1 = 'owen',player2 = 'jean'):
        self.rounds = rounds 
        self.steps = 5
        self.player1 = player1
        self.player2 = player2
    def print_players(self):
        """
        Print Players
        """
        print('{} is playing {}'.format(self.player1,self.player2))
    
    def add_round(self):
        """
        incrmenet number of rounds
        """
        self.rounds += 1 

    def winner(self):
        """"randomly pick and return winner"""
        return self.player1 if random() > 0.5 else self.player2


class Tic(Game):
    """
    Subclass of Game called Tictactoe
    """

    def __init__(self, rounds=3, player1 = 'Riley', player2 = 'Amer'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing TicTacToe with {}'.format(self.player1,self.player2))