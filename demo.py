def test_get_status(self):
        """
        Test getStatus()
        """

        self.player.setSetOfCards({(2, "DIAMONDS"), (3, "HEARTS")})

        # self.player.addCard((8, "SPADES"))

        self.assertEqual(self.player.getStatus(), PlayerStatus.HIT)