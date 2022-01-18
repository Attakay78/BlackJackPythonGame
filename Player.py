from functools import reduce

from PlayerStatus import PlayerStatus

class Player:
    def __init__(self, name: str) -> None:
        self.name : str = name
        self.set_of_cards : set = set()
        self.status : PlayerStatus = None
    
    def getName(self) -> str:
        return self.name

    def getScore(self) -> int :
        return reduce(lambda x, y : x + y , [item[0] for item in self.set_of_cards])

    def setSetOfCards(self, listOfCards : set) -> None:
        self.set_of_cards = listOfCards

    def getSetOfCards(self) -> set :
        return self.set_of_cards

    def addCard(self, card) -> None:
        self.set_of_cards.add(card)

    def setStatus(self, status) -> None :
        self.status = status

    def getStatus(self) -> PlayerStatus :
        return self.status

    # def changeStatus(self, new_status) -> None :
    #     self.status = new_status
        

    def __str__(self) -> str:
        return f"Name: {self.name}, score: {self.getScore()}, status: {self.getStatus()}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, score: {self.getScore()}, status: {self.getStatus()}"