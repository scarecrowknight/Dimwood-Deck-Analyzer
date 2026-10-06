from parser import Parser

class ArtifactParser(Parser):

    
    def parseArtifacts(self, playerText):
        numArtifacts, playerText = self.splitAtNAsInt(playerText, 2)

        
        artifacts = [] # the style on this is different from deck parser which is 
        # probably bad form so ill fix it soon
        for i in range(numArtifacts):
        
            artifactData, playerText = self.getNext(playerText)
        
            artifacts.append(self.parseArtifact(artifactData))
        
        
        # this is the pool of artifacts you'll get to choose from at the begining of next run. 
        # there are more intricacies you can read abt on the wiki but that's the simple version
        numNextRunArtifacts, playerText = self.splitAtNAsInt(playerText, 2)
        
        
        # not doing anything with this data yet. Maybe at some point I will tho so keeping this around instead ofjust cutting it out.
        nextRunartifacts = [] 
        for i in range(numNextRunArtifacts):
        
            dataLength, playerText = self.splitAtNAsInt(playerText, 2)
            artifactData, playerText = self.splitAtN(playerText, dataLength)

        
            nextRunartifacts.append(self.parseArtifact(artifactData))

        return artifacts, playerText

    
    def parseArtifact(self, artifactText):
        name, artifactText = self.getNext(artifactText)

        dataLength, artifactText = self.splitAtNAsInt(artifactText, 2)
        for i in range(dataLength):
            artifactExtraData, artifactText = self.getNext(artifactText)
            # here is where we could do something with the extra data..
            # honestly though, I'm pretty sure this is just scroll and charm, which aren't relevant to light changing ^^
        return name

        