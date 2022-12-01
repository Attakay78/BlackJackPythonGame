from sys import argv
from functools import reduce

from GameStatus import GameStatus
from Player import Player
from PlayerStatus import PlayerStatus
from Suits import Suit
from Face import Face
from random import shuffle

class Game:

    # Constructor with some instance variables
    def __init__(self, args) -> None:
        self.list_of_players = []
        self.list_of_names = args
        self.shuffled_deck = []
        self.players_hit = []
        self.players_stick = []
        self.players_bust = []
        self.game_status = None


    # Function to create deck of cards from Suit and Face enum constants
    def create_deck(self) -> list:
        retur [(int(face.value), suit.name) for suit in Suit for face in Face]


    # Function to shuffle deck of cards using shuffle method
    # from random module
    def shuffle_deck(self) -> list:
        new_deck : list = self.create_deck()
        shuffle(new_deck)
        return new_deck

    # Function to create players from names in list_of_names variable
    def create_players(self) -> None :
        for name in self.list_of_names:
            self.list_of_players.append(Player(name))


    # Players getter function
    def get_all_players(self) -> list:
        return self.list_of_players


    # Function to deal cards to players
    def deal_cards_to_players(self) -> None:
        for player in self.list_of_players:
            card1 : tuple = self.shuffled_deck.pop(0)
            card2 : tuple = self.shuffled_deck.pop(0)
            player.add_card(card1)
            player.add_card(card2)


    # Function to set player status based on current score
    def set_player_status(self, player : Player) -> None:
        # getting player score
        score = player.get_score()
        if(score < 17):
            player.set_status(PlayerStatus.HIT)
        elif(score >= 17 and score <= 21):
            player.set_status(PlayerStatus.STICK)
        else:
            player.set_status(PlayerStatus.BUST)
            

    # Function to start game
    def start(self) -> None :
        # Set game status to START
        self.game_status = GameStatus.START

        self.create_deck()
        self.shuffled_deck = self.shuffle_deck()
        self.create_players()

        # Set game status to IN_MOTION
        self.game_status = GameStatus.IN_MOTION

        self.deal_cards_to_players()
        
        # Looping over list of players and adding them to 
        # a list based on their status
        for player in self.list_of_players:
            self.set_player_status(player)
            status = player.get_status()

            if(status == PlayerStatus.HIT):
                self.players_hit.append(player)
            elif(status == PlayerStatus.STICK):
                self.players_stick.append(player)
            else:
                self.players_bust.append(player)


        # Loop for game to continue until game status changes to FINISH
        while(self.game_status != GameStatus.FINISH):
            
            # Checking for players with score equal 21 after dealing 
            # cards to players the first time
            scored_21 = []
            for player in self.players_stick:
                score = player.get_score()
                if(score == 21):
                    scored_21.append(player)

            if(len(scored_21) == 1):
                print(f"Game ended, won by {scored_21[0].get_name()} with score {scored_21[0].get_score()}")
                self.game_status = GameStatus.FINISH
            elif(len(scored_21) > 1):
                print("There is a tie")
                self.game_status = GameStatus.FINISH
            else:
                # Checking if all players got busted
                if(len(self.players_bust) == len(self.list_of_players)):
                    self.game_status = GameStatus.FINISH
                    print("No winner, All players busted!!!")

                # Checking if any player exist in players_hit list. Deal
                # cards to players until no player left in players_hit list
                elif(len(self.players_hit) > 0):

                    # Assign players_hit to new_players_hit to
                    # prevent concurrentModification error
                    new_players_hit : list = self.players_hit

                    while(len(new_players_hit) != 0):
                        for player in self.players_hit:
                            card : tuple = self.shuffled_deck.pop(0)
                            player.add_card(card)

                            self.set_player_status(player)

                            status = player.get_status()
                            
                            if(status == PlayerStatus.STICK):
                                # Remove players with new status STICK from players_hit
                                # to players_stick list
                                new_players_hit.remove(player)
                                self.players_stick.append(player)
                            elif(status == PlayerStatus.BUST):
                                # Remove players with new status BUST from players_hit
                                # to players_bust list
                                new_players_hit.remove(player)
                                self.players_bust.append(player)
                        
                        self.players_hit = new_players_hit
                else:
                    # Logic to check for game winner based on players
                    # in players_stick list with highest score or 
                    # players with same highest score
                    multi_winner : list = []
                    winner : Player = None
                    score : int = 0
                    for player in self.players_stick:
                        player_score = player.get_score()
                        if(player_score == score):
                            multi_winner.append(player)
                        if(player.get_score() > score):
                            multi_winner = []
                            multi_winner.append(player)
                            score = player.get_score()
                            winner = player

                    if(len(multi_winner) > 1):
                        print("There is a tie")
                    else:    
                        print(f"Game ended, won by {winner.get_name()} with score {winner.get_score()}")

                    self.game_status = GameStatus.FINISH
                
            
        print(self.list_of_players)    
        


if __name__ == "__main__":
    game = Game(argv[1:])
    game.start()

