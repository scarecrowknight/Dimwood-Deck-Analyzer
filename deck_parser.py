from card import Card
from parser import Parser

class DeckParser(Parser):

    def parseDeck(self, deckString) -> list[Card]:
        
        def parseCard(cardString) -> Card:
            # first line cuts off ID, art, frame, # pip mods
            # potential to expand functionality here.
            cardString = cardString[12:] 

            name, cardString = self.getNext(cardString)
            
            # 40 is chosen here because each card has 20 pip slots, each with a value 2 characters long.
            # So unless the max number of pips changes this should rmain reliable.
            pips, cardString = self.splitAtN(cardString, 40)

            #stamps, cardString = splitAtN(cardString, 10) 
            # parsing stamps requires another subfunction because of the way extra data is attatched to stamps in this game
            card = Card(name, pips)
            return card
        
        numCards, deckString = self.splitAtNAsInt(deckString,2)
        deck = list()

        for i in range(numCards):
            cardString, deckString = self.getNext(deckString)
            card = parseCard(cardString)
            deck.append(card)
        return deck
