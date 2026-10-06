from light import Light

class LightLevel:
    def __init__(self, startingLight):
        self.level = startingLight
        self.lockCount = 0
        # should take in a list of currently held artifacts to account for eclipse and such
    def bright(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.BRIGHT:
                self.level = Light.BRIGHT
            case Light.DIM:
                self.level = Light.BRIGHT
            case Light.DARK:
                self.level = Light.BRIGHT


    def dim(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.BRIGHT:
                self.level = Light.DIM
            case Light.DIM:
                self.level = Light.DIM
            case Light.DARK:
                self.level = Light.DIM

    def dark(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.BRIGHT:
                self.level = Light.DARK
            case Light.DIM:
                self.level = Light.DARK
            case Light.DARK:
                self.level = Light.DARK
    def up(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.BRIGHT:
                self.level = Light.BRIGHT
            case Light.DIM:
                self.level = Light.BRIGHT
            case Light.DARK:
                self.level = Light.DIM
    def down(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.BRIGHT:
                self.level = Light.DIM
            case Light.DIM:
                self.level = Light.DARK
            case Light.DARK:
                self.level = Light.DARK
    def lock(self):
        self.lockCount +=1