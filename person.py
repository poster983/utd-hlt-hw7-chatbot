import pickle


import pickle

class User():
    def __init__(self, name=None, hobby=None, characteristic=None, house=None, nickname=None):
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