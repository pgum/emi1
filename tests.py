import unittest
import game

class TestRzutyKostka(unittest.TestCase):

    #pierwszy test poprawiony i przechodzi!
    def test_rzutNieWiekszyNiz6(self):
        self.assertLess(game.rzut(), 7)

    #przy aktualnej "implementacji" ten test nie przejdze :(
    def test_rzutNieMniejszyNiz1(self):
        self.assertGreater(game.rzut(), 0)

if __name__ == '__main__':
    unittest.main()
