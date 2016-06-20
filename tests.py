import unittest
import game

class TestRzutyKostka(unittest.TestCase):

    #pierwszy test poprawiony i przechodzi!
    def test_rzutNieWiekszyNiz6(self):
        self.assertLess(game.rzut(), 7)

    #teraz przechodzi
    def test_rzutNieMniejszyNiz1(self):
        self.assertGreater(game.rzut(), 0)
    #po tych dwoch testach wiemy ze pojedynczy rzut koscia nie daje debilnych wynikow typu -1

class TestRunda(unittest.TestCase):
    def test_rundaMaDacPareWynikow(self):
        wyn_czlo, wyn_cpu= game.runda()
        self.assertTrue(wyn_czlo > 1)
        self.assertTrue(wyn_czlo < 13)
        self.assertTrue(wyn_cpu > 1)
        self.assertTrue(wyn_cpu < 13)

class TestGra(unittest.TestCase):
    def test_graKonczySieJednymZTrzechWynikow(self):
        wynik_gry= gra()
        self.assertTrue(wynik_gry == "Remis" or wynik_gry == "CPU" or wynik_gry == "Gracz")

#logika programu, że jak bedzie remis to ma losowac jeszcze raz nie ma sensu testowac w tak malym programie. Normalnie bysmy probowali robic wydmuszke z funkcji gra() zeby moc ja ustawic za pierwszym razem na "Remis" a potem a cos innego zeby zobaczyc jak zachowa sie funkcja main().


if __name__ == '__main__':
    unittest.main()
