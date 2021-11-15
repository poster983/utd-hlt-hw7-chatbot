import pickle

from thefuzz import process

class User():
    def __init__(self, name=None, hobby=None, character=None, house=None, nickname=None):
        self.name = name
        self.hobby = hobby
        self.character = character
        self._house = None
        self.house = house
        self.nickname = nickname

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, h):
        if h == None:
            self._house == h
            return
        values = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        fuzz = process.extractOne(h, values)
        if fuzz[1] < 50:
            self._house = None
        self._house = fuzz[0]

    def getName(self):
        return self.name

    def getNickName(self):
        return self.nickname

    def setName(self, name):
        self.name = name
        self.nickname = name

    def setHobby(self, hobby):
        self.hobby = hobby

    def getHobby(self):
        return self.hobby

    def setChar(self, character):
        self.character = character

    def getChar(self):
        return self.character



class UserBase():
    def __init__(self, filename="userbase.pickle"):
        self.filename = filename
        self.dict = {}
        try: 
            with open(self.filename, 'rb') as handle:
                self.dict = pickle.load(handle)
        except OSError as e:
            # File not found
            print("Need to make a file")

    #Take the data and save it to the self.dict variable where the key is the user_id
    #Save the self.dict to a pickle
    def update(self, user_id:str, data: User): 
        self.dict[user_id] = data
        with open(self.filename, 'wb') as handle:
            pickle.dump(self.dict, handle)
            
    # pull from self.dict and chack to see if it even exists in the dict. (avoid a key error)
    def get(self, user_id: str):
        return self.dict.get(user_id, User())