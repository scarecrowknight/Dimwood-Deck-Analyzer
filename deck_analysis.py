from light import Light
from light_level import LightLevel
from light_warnings import warnings
from card import Card
from pips import Pip
from savefile import SaveFile
# this class is still not cohesive and needs to be more broken up

def deckLightAnalysis(save: SaveFile, isEclipse: bool = False) -> list:
    artifacts = save.artifacts
    deck = save.deck

    # maybe modify output later or be responsible and put it in an object now. maybe output 3x3 array

    # 2d array of all deck entries
    entryGraph = []

    lightMatrix = [[0,0,0],[0,0,0],[0,0,0]]
    for card in deck:
        # recall that the light values from cardLightAnalysis(card) represent endstates 
        # starting from from bright, dim, and dark respectively

        #WILL NEED AN OVERHAUL WITH STAMP UPDATE


        stanceDance = cardLightAnalysis(card, artifacts)
        entryGraph.append(stanceDance)
        for i in range(3):
            start = i
            end = (stanceDance[i].value)
            lightMatrix[start][end]+=1
    
    
    warnings(lightMatrix)
    
    return lightMatrix


def cardLightAnalysis(card: Card, artifacts: list[str], isEclipse: bool = False) -> list[Light]:
    #once we have stamp info this will have to turn into a switch case statement T_T
    
    # I'm not implementing pip shaker, you can't make me

    # don't yet have a save to test flourish. Come back to this
    if ("flourish" in artifacts) and (card.phrases[0][0] == Pip.Empty):
        lightPhrase = card.phrases[Light.LIGHT.value+1] * 2
        dimPhrase = card.phrases[Light.DIM.value+1] * 2
        darkPhrase = card.phrases[Light.DARK.value+1] * 2
    else:
        lightPhrase = card.phrases[0] + card.phrases[Light.LIGHT.value+1]
        dimPhrase = card.phrases[0] + card.phrases[Light.DIM.value+1]
        darkPhrase = card.phrases[0] + card.phrases[Light.DARK.value+1]

    stanceDance = []
    stanceDance.append(parseLight(lightPhrase, Light.LIGHT, artifacts, isEclipse))
    stanceDance.append(parseLight(dimPhrase, Light.DIM, artifacts, isEclipse))
    stanceDance.append(parseLight(darkPhrase, Light.DARK, artifacts, isEclipse))
    
    return stanceDance


def parseLight(fullPhrase: list[Pip], startingLight: Light, artifacts: str, isEclipse: bool) -> Light:

    lightLevel = LightLevel(startingLight, artifacts, isEclipse)
    
    for pip in fullPhrase:
        match (pip):
            case Pip.Light:
                lightLevel.light()     
            case Pip.Dim:
                lightLevel.dim()
            case Pip.Dark:
                lightLevel.dark()
            case Pip.Lighten:
                lightLevel.up()
            case Pip.Darken:
                lightLevel.down()
            case Pip.Lock:
                lightLevel.lock()
            case _:
                pass
    return lightLevel.level 