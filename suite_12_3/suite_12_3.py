# suite_12_3.py

import unittest
import runner_test
import tournament_test


def load_tests(loader, tests, pattern):
    # Создайте модуль suite_12_3.py для описания объекта TestSuite.
    # Укажите на него переменной с произвольным названием.
    suite = unittest.TestSuite()
    # Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
    suite.addTests(loader.loadTestsFromTestCase(runner_test.RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(tournament_test.TournamentTest))
    return suite


if __name__ == '__main__':
    # Создайте объект класса TextTestRunner, с аргументом verbosity=2.
    runner = unittest.TextTestRunner(verbosity=2)
    # Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
    runner.run(load_tests(unittest.TestLoader(), None, None))

# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s

# OK (skipped=3)
