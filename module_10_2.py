import threading
import time


class Knight(threading.Thread):
    total_enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies_remaining = Knight.total_enemies

        while enemies_remaining > 0:
            self.days += 1
            time.sleep(1)
            enemies_remaining -= self.power
            enemies_remaining = max(0, enemies_remaining)
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies_remaining} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
