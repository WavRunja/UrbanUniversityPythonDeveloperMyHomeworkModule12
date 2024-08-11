# Код runner_and_tournament.py исправленный.

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    # def __str__(self):
    #     return self.name

    def __str__(self):
        # return f"Runner(name={self.name}, speed={self.speed})"
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

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
        # print("self", self)
        finishers = {}
        # print("finishers", finishers)
        place = 1
        # print("place", place)
        while self.participants:
            # print("self.participants", self.participants)
            # Нарезка — важная концепция Python,
            # которая позволяет нам выбирать определенные элементы из списка,
            # кортежа или строки. Это делается с помощью оператора нарезки [:].
            # Оператор принимает два аргумента, разделенных двоеточием.
            # Используем копию списка для итерации.
            for participant in self.participants[:]:
                # print("participant", participant)
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    # print(f"finishers[{place}] = {finishers[place]}")
                    place += 1
                    # print(f"place + 1 = {place}")
                    self.participants.remove(participant)
                    # print("finishers", finishers)
                    # Ошибка, все обновления происходят в одном цикле,
                    # при увеличении дистанции у всех участников одновременно,
                    # участники с большей скоростью могут финишировать позже,
                    # чем участники с меньшей скоростью.
        return finishers
