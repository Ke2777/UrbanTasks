import unittest
from module_12_2 import Runner, Tournament


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, 'is_frozen', False):
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result_name, results in cls.all_results.items():
            print(f"Результаты для {result_name}: {results}")

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    # @skip_if_frozen
    # def test_challenge(self):
    #     tournament = Tournament(90, self.runner_usain, self.runner_nick)
    #     results = tournament.start()
    #     self.__class__.all_results["Турнир Усэйн и Ник"] = {place: str(runner) for place, runner in results.items()}
    #     self.assertTrue(results[max(results)].name == "Ник")


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result_name, results in cls.all_results.items():
            print(f"Результаты для {result_name}: {results}")

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Турнир Усэйн и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results)].name == "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Турнир Андрей и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results)].name == "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Турнир Усэйн, Андрей и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results)].name == "Ник")


if __name__ == "__main__":
    unittest.main()
