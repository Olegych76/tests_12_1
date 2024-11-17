import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.runner = Runner("Леонардо")
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50, 'Дистанция должна быть 50 после 10 прогулок')

    def test_run(self):
        self.runner = Runner("Донателло")
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100, 'Дистанция должна быть 100 после 10 пробежек')

    def test_challenge(self):
        self.runner1 = Runner("Микеланджело")
        self.runner2 = Runner("Рафаэль")
        for _ in range(10):
            self.runner1.walk()
            self.runner2.run()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance, 'Дистанция должна быть разная')


if __name__ == "__main__":
    unittest.main()
