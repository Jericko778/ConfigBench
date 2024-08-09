class Config:
    configs = []

    def __init__(self, symbol, hasConfigs = False, subconfigs = None):
        self.symbol = symbol
        self.hasConfigs = hasConfigs
        self.subconfigs = subconfigs
        Config.configs.append(self)

    def getSymbol(self):
        return self.symbol

    def hasSubconfigs(self):
        return self.hasConfigs

    def getSubconfigs(self):
        return self.subconfigs
    
    def __str__(self):
        return self.symbol + " " + str(self.subconfigs)