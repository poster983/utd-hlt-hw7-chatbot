class User():
    def __init__(self, name, hobby, characteristic, house, nickname):
        self.name = name
        self.hobby = hobby
        self.characteristic = characteristic
        self.house = house
        self.nickname = nickname

    def getName(self):
        return self.name

    def getNickName(self):
        return self.nickname

    def setName(self, name):
        self.name = name
        self.nickname = name

    def setHouse(self, house):
        self.house = house

    def getHouse(self):
        return self.house

    def setHobby(self, hobby):
        self.hobby = hobby

    def getHobby(self):
        self.hobby

    def setChar(self, characteristic):
        self.characteristic = characteristic

    def getChar(self):
        return self.characteristic
