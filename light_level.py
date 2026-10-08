from light import Light

class LightLevel:
    def __init__(self, startingLight, artifacts, isEclipse: bool = False):
        self.level = startingLight
        self.lockCount = 0
        self.artifacts = artifacts
        self.isEclipse = isEclipse
        # should take in a list of currently held artifacts to account for eclipse and such
    
    def light(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        else:
            self.level = Light.LIGHT

    def dim(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        else:
            self.level = Light.DIM
            

    def dark(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        else:
            self.level = Light.DARK

    def up(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.LIGHT:
                if("Solar Eclipse" in self.artifacts):
                    self.level = Light.DARK
                else:
                    pass

            case Light.DIM:
                self.level = Light.LIGHT
            
            case Light.DARK:
                self.level = Light.DIM

    def down(self):
        if(self.lockCount>0):
            self.lockCount-=1
            return
        match(self.level):
            case Light.LIGHT:
                self.level = Light.DIM
            case Light.DIM:
                self.level = Light.DARK
            case Light.DARK:
                if(("Lunar Eclipse" in self.artifacts) or (isEclipse)):
                    self.level = Light.LIGHT
                else:
                    pass
    
    def lock(self):
        self.lockCount +=1