from enum import Enum
class Pip(Enum):
    Empty = 0
    Light = 1
    Dim = 2
    Dark = 3
    Lighten = 4 
    Darken = 5
    Damage = 6
    Mushroom = 7
    Hurt = 8
    Lifesteal = 9
    Heal = 10 
    Block = 11
    Bi_Block = 12
    Tri_Damage = 13
    Poison = 14
    Lock = 15
    Energy = 16
    Draw = 17
    Exhaust = 18
    Consume = 19 
    Coin = 20
    Bargain = 21

    def getInverse(self):
        match(self):
            case(Pip.Light):
                return Pip.Dark
            
            case(Pip.Dark):
                return Pip.Light
            
            case(Pip.Lighten):
                return Pip.Darken
            
            case(Pip.Darken):
                return Pip.Lighten
            
            # all non light pips are left the same when inverted
            case _:
                return self


def main():
    darken = Pip.Darken
    print(darken.getInverse())


if __name__ == "__main__":
    main()