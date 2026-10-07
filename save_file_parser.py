#standard packages
from pathlib import Path

#local packages
from savefile import SaveFile
from deck_analysis import deckLightAnalysis
from deck_parser import DeckParser
from artifact_parser import ArtifactParser
from parser import Parser



class SaveFileParser(Parser):

    def parseSave(self):
            playerText = self.saveFileStringExtracter()
            save = self.parsePlayerText(playerText)
            return save
    
    # should use adapter style to add drag and drop functionality to website 
    def saveFileStringExtracter(self):
        saveDirectory = str(Path(r"C:\Users\Siris\OneDrive\Desktop\csci for fun\dimwood programs\savedata"))
        
        with open(saveDirectory, encoding="utf8") as f:
            playerText = f.read()
            return playerText
        
    
    
    def parsePlayerText(self, playerText):
        index = playerText.find("--player")
        playerText = playerText[index+9:] #everything before and including "\n--player" is junk data for us ^^

        nameLength, playerText = self.splitAtNAsInt(playerText,2)
        name, playerText = self.splitAtN(playerText, nameLength)
        
        playerText = playerText[176:] # subject to change, ink told me this length of garbage bytes to ignore

        
        artifactParser = ArtifactParser()
        artifacts, playerText = artifactParser.parseArtifacts(playerText)

        print(artifacts)

        deckParser = DeckParser()
        deck = deckParser.parseDeck(playerText)
        lightMatrix = deckLightAnalysis(deck)
        save = SaveFile(name, deck, artifacts, lightMatrix)
        return save


#fun fact, this is basically just a very complex push down automota ^^ which means that Dimwood save files are CFGs :p