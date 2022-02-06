from functools import reduce

from PlayerStatus import PlayerStatus

class Player:
    def __init__(self, name: str) -> None:
        self.name : str = name
        self.set_of_cards : set = set()
        self.status : PlayerStatus = None
    
    def get_name(self) -> str:
        return self.name

    def get_score(self) -> int :
        return reduce(lambda x, y : x + y , [item[0] for item in self.set_of_cards])

    def set_set_of_cards(self, listOfCards : set) -> None:
        self.set_of_cards = listOfCards

    def get_set_of_cards(self) -> set :
        return self.set_of_cards

    def add_card(self, card) -> None:
        self.set_of_cards.add(card)

    def set_status(self, status) -> None :
        self.status = status

    def get_status(self) -> PlayerStatus :
        return self.status
        

    def __str__(self) -> str:
        return f"Name: {self.name}, score: {self.get_score()}, status: {self.get_status()}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, score: {self.get_score()}, status: {self.get_status()}"