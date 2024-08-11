# tests_12_1.py
# test_runner.py
import unittest
# Выполняя правки одноимённых классов Runner в модулях runner и tournament,
# гипотетически, здесь можно искусственно создать Ад для тестировщика.
# from runner import Runner
from tournament import Runner


# Домашнее задание по теме "Простые Юнит-Тесты"

# Задача "Проверка на выносливость".

# Напишите соответствующий декоратор к каждому методу (кроме @classmethod),
def freeze_check(func):
    # который при значении is_frozen = False будет выполнять тесты,
    def wrapper(self, *args, **kwargs):
        # а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        # is_frozen = False - будет выполнять тесты.
        return func(self, *args, **kwargs)

    return wrapper


# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
class RunnerTest(unittest.TestCase):
    # Класс RunnerTest дополнить атрибутом is_frozen = False.
    # Вы можете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута is_frozen.
    # При значении is_frozen = False TestCase будет выполнять тесты, а is_frozen = True - пропускать.
    is_frozen = False

    @freeze_check
    # test_walk - метод, в котором
    def test_walk(self):
        # создаётся объект класса Runner с произвольным именем.
        runner = Runner("ArbitraryRunnerName")
        # Далее вызовите метод walk у этого объекта 10 раз.
        for _ in range(10):
            runner.walk()
        # После чего методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(runner.distance, 50)

    @freeze_check
    # test_run - метод, в котором
    def test_run(self):
        # создаётся объект класса Runner с произвольным именем.
        runner = Runner("ArbitraryRunnerName")
        # Далее вызовите метод run у этого объекта 10 раз.
        for _ in range(10):
            runner.run()
        # После чего методом assertEqual сравните distance этого объекта со значением 100.
        self.assertEqual(runner.distance, 100)

    @freeze_check
    # test_challenge - метод в котором
    def test_challenge(self):
        # создаются 2 объекта класса Runner с произвольными именами.
        runner1 = Runner("ArbitraryRunnerName1")
        runner2 = Runner("ArbitraryRunnerName2")

        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
        # чтобы убедится в неравенстве результатов.
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)


if __name__ == '__main__':
    # Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
    unittest.main()
    # test_walk()
    # test_run()
    # test_challenge()
    # Вывод на консоль:
    # Ran 3 tests in 0.001s OK
