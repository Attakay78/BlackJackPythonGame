import unittest
from Player import Player
# from PlayerStatus import PlayerStatus

class TestPlayer(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        """ 
        Runs once at the very beginning before the test
        """
        print("Start Test")


    @classmethod
    def tearDownClass(cls) -> None:
        """ 
        Runs once at the very end after the test
        """
        print("End Test")

    def setUp(self) -> None:
        self.player = Player("Player 1")

    def tearDown(self) -> None:
        pass


    def test_player_stats(self) -> None:
        """ 
        Test player stats 
        """

        self.assertEqual(self.player.getName(), 'Player 1')
        self.assertEqual(self.player.set_of_cards, set())  
        self.assertEqual(self.player.status, None)


    def test_set_set_of_card(self) -> None:
        """ 
        Test setSetOfCards()
        """

        self.player.setSetOfCards({(2, "DIAMONDS"), (3, "HEARTS")})

        self.assertEqual(self.player.getSetOfCards(), {(2, "DIAMONDS"), (3, "HEARTS")})
    

    def test_add_card(self) -> None:
        """
        test addCard()
        """

        self.player.setSetOfCards({(2, "DIAMONDS"), (3, "HEARTS")})

        self.player.addCard((8, "SPADES"))

        self.assertEqual(self.player.getSetOfCards(), {(2, "DIAMONDS"), (3, "HEARTS"), (8, "SPADES")})


    def test_get_score(self):
        """
        Test getScore()
        """

        self.player.setSetOfCards({(2, "DIAMONDS"), (3, "HEARTS")})

        self.player.addCard((8, "SPADES"))

        self.assertEqual(self.player.getScore(), 13)

    


if __name__ == '__main__':
    unittest.main()