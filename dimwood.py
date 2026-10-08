from save_file_parser import SaveFileParser
import deck_analysis
def main():
    saveParser = SaveFileParser()
    save = saveParser.parseSave()
    print(save)
    print(deck_analysis.deckLightAnalysis(save))
    print("----")
    print(deck_analysis.deckLightAnalysis(save, isEclipse=True))
    #these are all my test cases :)
    
    #cardstr = "55001C00EC030007top hat0F040600000000000000000000000000000000001F002A001A00220000000000"
    #deckLightAnalysis(deck)





if __name__ == '__main__':
    main()


