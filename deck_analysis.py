from light import Light
from light_level import LightLevel
from light_warnings import warnings
from card import Card

# this class is still not cohesive and needs to be more broken up

def deckLightAnalysis(deck: list[Card]) -> list:
    def cardLightAnalysis(card: Card) -> list[Light]:
        #once we have stamp info this will have to turn into a switch case statement T_T
        
        Bright = card.phrases[0] + card.phrases[Light.BRIGHT.value+1]
        Dim = card.phrases[0] + card.phrases[Light.DIM.value+1]
        Dark = card.phrases[0] + card.phrases[Light.DARK.value+1]
        

        # could be condensed for light dim dark. standardization is nice though... 
        def parseLight(fullPhrase: list, startingLight: Light) -> Light:
            

            lightLevel = LightLevel(startingLight) #starting light must be 1, 2 3
           
            for pip in fullPhrase:
                match (pip.value):
                    case 1:
                        lightLevel.bright()     
                    case 2:
                        lightLevel.dim()
                    case 3:
                        lightLevel.dark()
                    case 4:
                        lightLevel.up()
                    case 5:
                        lightLevel.down()
                    case 15:
                        lightLevel.lock()
                    case _:
                        pass
            return lightLevel.level 
            

        stanceDance = []
        stanceDance.append(parseLight(Bright, Light.BRIGHT))
        stanceDance.append(parseLight(Dim, Light.DIM))
        stanceDance.append(parseLight(Dark, Light.DARK))
        
        return stanceDance

    # maybe modify output later or be responsible and put it in an object now. maybe output 3x3 array
    
    # could be useful for calculations later: numCards = len(deck)

    # 2d array of all deck entries
    entryGraph = []


    # for eclipse I have an idea. 
    # Instead of implementing it twice for each half eclipse variant we can just implement half eclipse once and then
    # run it again on an entirely inverted deck if they have the opposite half eclipse relic B) 
    lightMatrix = [[0,0,0],[0,0,0],[0,0,0]]
    for card in deck:
        # recall that the light values from cardLightAnalysis(card) represent endstates 
        # starting from from bright, dim, and dark respectively

        #WILL NEED AN OVERHAUL WITH STAMP UPDATE


        stanceDance = cardLightAnalysis(card)
        entryGraph.append(stanceDance)
        for i in range(3):
            start = i
            end = (stanceDance[i].value)
            lightMatrix[start][end]+=1
    
    
    warnings(lightMatrix)
    
    return lightMatrix

