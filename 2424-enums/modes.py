# https://youtube.com/@Carberra

from enum import Enum, auto


class GameState(Enum):
    PAUSED = auto()
    PLAYING = auto()
    GAMEOVER = auto()


if __name__ == "__main__":
    print(GameState.PLAYING)
    print(GameState.PAUSED.name)
    print(GameState.GAMEOVER.value)

    print(GameState(1))
    print(GameState["PLAYING"])
