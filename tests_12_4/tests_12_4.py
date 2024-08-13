# tests_12_4.py

# Домашнее задание по теме "Логирование".

# Задача "Логирование бегунов".

import unittest
# В модуле tests_12_4.py импортируйте пакет logging.
import logging
from rt_with_exceptions import Runner

# Настройте basicConfig на следующие параметры:
logging.basicConfig(
    # 1. Уровень - INFO.
    level=logging.INFO,
    # 2. Режим - чтение
    # Внимание! В данном пункте ошибка в условии задачи: необходимо заменить слово "чтение" на "запись".
    filemode="w",
    # 3. Название файла - runner_tests.log
    filename='runner_tests.log',
    # 4. Кодировка - UTF-8
    encoding='utf-8',
    # 5. Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
    format='%(asctime)s | %(levelname)s | %(message)s'
)


def freeze_check(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_check
    # Дополните методы тестирования в классе RunnerTest следующим образом:
    # test_walk:
    def test_walk(self):
        # 1. Оберните основной код конструкцией try-except.
        try:
            # 2. При создании объекта Runner передавайте отрицательное значение в speed.
            runner = Runner("TestRunner", -5)  # Скорость = -5
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            # 3. В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # 4. В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
            # с сообщением "Неверная скорость для Runner".
            logging.warning(f'Неверная скорость для Runner: {e}')
            self.fail(f'Test failed due to exception: {e}')

    @freeze_check
    # Дополните методы тестирования в классе RunnerTest следующим образом:
    # test_walk:
    def test_run(self):
        # 1. Оберните основной код конструкцией try-except.
        try:
            # 2. При создании объекта Runner передавайте что-то кроме строки в name.
            runner = Runner(1234, 5)  # Некорректное имя
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            # 3. В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'.
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # 4. В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
            # с сообщением "Неверный тип данных для объекта Runner".
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')
            # Внимание! Ошибка в шестой строке файла rt_with_exceptions.py:
            # необходимо заменить слово "числом" на "строкой".
            self.fail(f'Test failed due to exception: {e}')

    @freeze_check
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
