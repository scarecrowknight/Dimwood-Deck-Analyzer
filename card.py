from pips import Pip

class Card:
    def __init__(self, name: str, pips: list[Pip]):
        self.name = name        
        self.phrases = list[Pip]()
        # phrases[0] is always
        self.phrases.append(pips[:5])
        # phrases[1] is bright
        self.phrases.append(pips[5:10])
        # phrases[2] is dim
        self.phrases.append(pips[10:15])
        # phrases[3] is dark
        self.phrases.append(pips[15:20])

        #there are two main ways to go about saving the phrases:
        # 1) top to bottom as you read it in game.
        #   this is somewhat more intuitive, 
        #   but it leads to bright_phrase = phrases[light.BRIGHT.value + 1] which is a bit odd
        #
        # 2) in line with the light enums so that phrases[light.BRIGHT.value] = bright phrase
        #   this is probabl less intuitive but it makes for easier coding. 
        