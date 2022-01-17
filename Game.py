from sys import argv, exit
from functools import reduce

from GameStatus import GameStatus
from Player import Player
from PlayerStatus import PlayerStatus
from Suits import Suit
from Face import Face
from random import shuffle

class Game:
    def __init__(self, args) -> None:
        self.list_of_players = []
        self.list_of_names = args
        self.shuffled_deck = None
        self.players_hit = []
        self.players_stick = []
        self.players_bust = []
        self.game_status = None


    def createDeck(self) -> list:
        return [(int(face.value), suit.name) for suit in Suit for face in Face]


    def shuffleDeck(self) -> list:
        new_deck : list = self.createDeck()
        shuffle(new_deck)
        return new_deck


    def createPlayers(self) -> None :
        for name in self.list_of_names:
            self.list_of_players.append(Player(name))


    def getAllPlayers(self) -> list:
        return self.list_of_players

    def dealCardsToPlayers(self) -> None:
        for player in self.list_of_players:
            card1 : tuple = self.shuffled_deck.pop(0)
            card2 : tuple = self.shuffled_deck.pop(0)
            player.addCard(card1)
            player.addCard(card2)
            
    def start(self) -> None :
        self.game_status = GameStatus.START

        self.createDeck()
        self.shuffled_deck = self.shuffleDeck()
        self.createPlayers()

        self.game_status = GameStatus.IN_MOTION

        self.dealCardsToPlayers()
        
        while(self.game_status != GameStatus.FINISH):
            for player in self.list_of_players:
                status : PlayerStatus = player.getStatus()
                if(status == PlayerStatus.HIT):
                    self.players_hit.append(player)
                elif(status == PlayerStatus.STICK):
                    self.players_stick.append(player)
                else:
                    self.players_bust.append(player)
            
            if(len(self.players_bust) == 3):
                self.game_status = GameStatus.FINISH
                print("No winner, All players busted!!!")
            elif(len(self.players_hit) > 0):
                for player in self.players_hit:
                    card : tuple = self.shuffled_deck.pop(0)
                    player.addCard(card)
            else:
                winner = None
                score = 0
                for player in self.players_stick:
                    if(player.getScore() > score):
                        score = player.getScore()
                        winner = player
                
                self.game_status = GameStatus.FINISH

                print(f"Game ended, won by {winner.getName()} with score {winner.getScore()}")
                
            
        print(self.list_of_players)    
        


game = Game(argv[1:])
game.start()

