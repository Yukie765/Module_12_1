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
        runner= Runner('Vasya')
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_walk_broken(self):
        runner = Runner('Vasya')
        for i in range(0, 10):
            runner.walk()
        self.assertEqual(runner.distance, 150)

    def test_run(self):
        runner = Runner('Vasya')
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_chellange(self):
        runner1 = Runner('Vasya')
        runner2 = Runner('Andrey')
        for i in range(0, 10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)

if __name__ == '__main__':
    unittest.main()