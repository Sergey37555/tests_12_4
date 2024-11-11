import logging

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s: %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest:
    def test_walk(self):
        logging.info('"test_walk" выполнен успешно')
        try:
            runner = Runner('Test', -1)
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    def test_run(self):
        logging.info('"test_run" выполнен успешно')
        try:
            runner = Runner(123, 5)
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')


# Вызываем методы тестирования
if __name__ == "__main__":
    test = RunnerTest()
    test.test_walk()
    test.test_run()