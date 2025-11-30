import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*pl.split('; ')) for pl in lst_in]
players_filtered = list(filter(bool, players))
