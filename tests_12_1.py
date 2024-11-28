from unittest import TestCase, main
import module_12_1 as m12_1


class RunnerTest(TestCase):
    def test_walk(self):
        runner = m12_1.Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = m12_1.Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = m12_1.Runner("Runner1")
        runner2 = m12_1.Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    main()
