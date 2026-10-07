from enum import Enum
class Light(Enum):
    BRIGHT = 0
    DIM = 1
    DARK = 2
# note to future me, enums are itterable in top to bottom order!
# so in the future we can have:
# for light in Light:
# and it will itterate over BRIGHT, DIM DARK, from top to bottom    

