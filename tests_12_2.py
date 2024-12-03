import unittest
from module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        last_runner = results[max(results)].name
        self.assertTrue(last_runner == "Ник")

    def test_andrei_and_nick(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: str(runner) for place, runner in results.items()}
        last_runner = results[max(results)].name
        self.assertTrue(last_runner == "Ник")

    def test_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: str(runner) for place, runner in results.items()}
        last_runner = results[max(results)].name
        self.assertTrue(last_runner == "Ник")


if __name__ == "__main__":
    unittest.main()
