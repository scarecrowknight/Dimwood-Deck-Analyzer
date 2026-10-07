from card import Card
from parser import Parser
from pips import Pip

class DeckParser(Parser):

    def parseDeck(self, deckString) -> list[Card]:
        
        numCards, deckString = self.splitAtNAsInt(deckString,2)
        deck = list()

        for i in range(numCards):
            cardString, deckString = self.getNext(deckString)
            card = self.parseCard(cardString)
            deck.append(card)
        return deck

    def parseCard(self, cardString) -> Card:



        # first line cuts off ID, art, frame, # pip mods
        # potential to expand functionality here.
        cardString = cardString[12:] 

        name, cardString = self.getNext(cardString)

        # 40 is chosen here because each card has 20 pip slots, each with a value 2 characters long.
        # So unless the max number of pips changes this should rmain reliable.
        pips, cardString = self.splitAtN(cardString, 40)
        pips = self.parsePips(pips)

        #stamps, cardString = splitAtN(cardString, 10) 
        # parsing stamps requires another subfunction because of the way extra data is attatched to stamps in this game

        card = Card(name, pips)

        return card

    def parsePips(self, pips: str) -> list[Pip]:

        numPips = int(float(len(pips))*.5)
        allPhrases = list()

        for i in range(numPips):
            pip = (pips[2*i:2*i+2])
            pip = Pip(int(pip, 16))
            allPhrases.append(pip)

        return allPhrases




def main():
    deckstr = "0D55001C00EC030007top hat04060600000000000000000000000000000000001F002A001A0022000000000059001D00ED02010Bpick a card000000000000000000001111111100000000000023000000000000000000000057001A00EB020009spellcast00000000000C13030B0006060000000D1301060023000000000000000000000057001A00EB020009spellcast00000000000C13030B0006060000000D1301060023000000000000000000000057001A00EB020009spellcast00000000000C13030B0006060000000D1301060023000000000000000000000057001A00EB020009spellcast00000000000C13030B0006060000000D1301060023000000000000000000000055001B00EE020007twiddle0C0400000002000000000000000000000000000000000000000000000000000055001B00EE020007twiddle0C0400000002000000000000000000000000000000000000000000000000000055001B00EE020007twiddle0C0400000002000000000000000000000000000000000000000000000000000055001B00EE020007twiddle0C0400000002000000000000000000000000000000000000000000000000000059001E00EF02020Bfog machine030B101100070B0000000F0B000000020B00000000000000000000000000000859001E00EF02000Bfog machine030B000000070B0000000F0B000000020B00000000000000000000000000000054015200AF0F0106dimrot000000000000000000000000000000000000000017004D000000000000000000"
    deckParser = DeckParser()
    deck = deckParser.parseDeck(deckstr)
    card = deck[6]
    print(card.name)
    for phrase in card.phrases:
        print(phrase)
    card.invert()
    for phrase in card.phrases:
        print(phrase)


if __name__ == "__main__":
    main()