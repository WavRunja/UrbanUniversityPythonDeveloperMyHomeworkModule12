# tests_12_2.py

# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
from runner_test import freeze_check
from tournament import Runner, Tournament


# Код для тестирования.
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
class TournamentTest(unittest.TestCase):
    # Класс TournamentTest дополнить атрибутом is_frozen = True.
    # Вы можете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута is_frozen.
    # При значении is_frozen = False TestCase будет выполнять тесты, а is_frozen = True - пропускать.
    is_frozen = True
    # classmethod(function) -> method
    # Преобразует функцию в метод класса.
    # Метод класса получает класс как неявный первый аргумент,
    # так же как метод экземпляра получает экземпляр.

    @classmethod
    # setUpClass - метод, где создаётся атрибут класса all_results.
    def setUpClass(cls):
        # Это словарь в который будут сохраняться результаты всех тестов.
        cls.all_results = {}

    # setUp - метод, где создаются 3 объекта:
    def setUp(self):
        # Бегун по имени Усэйн, со скоростью 10.
        self.runner_usain = Runner("Усэйн", speed=10)
        # Бегун по имени Андрей, со скоростью 9.
        self.runner_andrei = Runner("Андрей", speed=9)
        # Бегун по имени Ник, со скоростью 3.
        self.runner_nik = Runner("Ник", speed=3)

    # Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
    # 1. Усэйн и Ник

    @freeze_check
    # Методы тестирования забегов,
    def test_usain_and_nik(self):
        # в которых создаётся объект Tournament на дистанцию 90.
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        # У объекта класса Tournament запускается метод start,
        result = tournament.start()
        # который возвращает словарь в переменную all_results.
        TournamentTest.all_results["test_usain_and_nik"] = result
        # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
        # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
        self.assertTrue(result[max(result.keys())] == "Ник")

    @freeze_check
    # Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
    # 2. Андрей и Ник.
    def test_andrei_and_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_andrei_and_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @freeze_check
    # Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
    # 3. Усэйн, Андрей и Ник.
    def test_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_usain_andrei_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @classmethod
    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            # print(f"{key}: {result}")
            print(f"{result}")


if __name__ == "__main__":
    unittest.main()

# Вывод на консоль:
# {1: Андрей, 2: Ник}
# {1: Усэйн, 2: Ник}
# {1: Усэйн, 2: Андрей, 3: Ник}

# Ran 3 tests in 0.001s
# OK
