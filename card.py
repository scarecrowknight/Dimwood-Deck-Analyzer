
class Card:
    def __init__(self, name, pips):
        self.name = name        
        self.phrases = list()
        self.phrases.append(pips[:10])
        self.phrases.append(pips[10:20])
        self.phrases.append(pips[20:30])
        self.phrases.append(pips[30:40])