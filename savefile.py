from card import Card

class SaveFile:
    def __init__(self, name, deck, artifacts, lightMatrix):
        self.name = name
        self.deck: list[Card] = deck
        self.artifacts = artifacts
        self.lightMatrix = lightMatrix