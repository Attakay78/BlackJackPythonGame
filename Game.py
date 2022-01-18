from sys import argv
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
        self.shuffled_deck = []
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


    def setPlayerStatus(self, player : Player) -> None:
        score = player.getScore()
        if(score < 17):
            player.setStatus(PlayerStatus.HIT)
        elif(score >= 17 and score <= 21):
            player.setStatus(PlayerStatus.STICK)
        else:
            player.setStatus(PlayerStatus.BUST)
            

    def start(self) -> None :
        self.game_status = GameStatus.START

        self.createDeck()
        self.shuffled_deck = self.shuffleDeck()
        self.createPlayers()

        self.game_status = GameStatus.IN_MOTION

        self.dealCardsToPlayers()
        
        for player in self.list_of_players:
            self.setPlayerStatus(player)
            status = player.getStatus()

            if(status == PlayerStatus.HIT):
                self.players_hit.append(player)
            elif(status == PlayerStatus.STICK):
                self.players_stick.append(player)
            else:
                self.players_bust.append(player)


        while(self.game_status != GameStatus.FINISH):
            
            scored_21 = []
            for player in self.players_stick:
                score = player.getScore()
                if(score == 21):
                    scored_21.append(player)

            if(len(scored_21) == 1):
                print(f"Game ended, won by {scored_21[0].getName()} with score {scored_21[0].getScore()}")
                self.game_status = GameStatus.FINISH
            elif(len(scored_21) > 1):
                print("There is a tie")
                self.game_status = GameStatus.FINISH
            else:
                if(len(self.players_bust) == len(self.list_of_players)):
                    self.game_status = GameStatus.FINISH
                    print("No winner, All players busted!!!")

                elif(len(self.players_hit) > 0):
                    new_players_hit : list = self.players_hit

                    while(len(new_players_hit) != 0):
                        for player in self.players_hit:
                            card : tuple = self.shuffled_deck.pop(0)
                            player.addCard(card)

                            self.setPlayerStatus(player)

                            status = player.getStatus()
                            
                            if(status == PlayerStatus.STICK):
                                new_players_hit.remove(player)
                                self.players_stick.append(player)
                            elif(status == PlayerStatus.BUST):
                                new_players_hit.remove(player)
                                self.players_bust.append(player)
                        
                        self.players_hit = new_players_hit
                else:
                    multi_winner : list = []
                    winner : Player = None
                    score : int = 0
                    for player in self.players_stick:
                        player_score = player.getScore()
                        if(player_score == score):
                            multi_winner.append(player)
                        if(player.getScore() > score):
                            multi_winner = []
                            multi_winner.append(player)
                            score = player.getScore()
                            winner = player

                    if(len(multi_winner) > 1):
                        print("There is a tie")
                    else:    
                        print(f"Game ended, won by {winner.getName()} with score {winner.getScore()}")

                    self.game_status = GameStatus.FINISH
                
            
        print(self.list_of_players)    
        


game = Game(argv[1:])
game.start()

