import random
import time

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


class ConfigMeta(type):
    @property
    def FRUIT(cls) -> str:
        print("Choosing fruit...")
        time.sleep(1)
        return random.choice(fruits)


class Config(metaclass=ConfigMeta):
    pass


if __name__ == "__main__":
    # print(Config.FRUIT)
    help(Config)
