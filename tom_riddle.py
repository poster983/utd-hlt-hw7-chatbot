# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2021 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

from chatterbot import ChatBot
from nltk.chat.util import Chat, reflections
import pickle
from FuzzySearch import FuzzySearch
from person import UserBase
   # test
# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.


class TomRiddle:
    def __init__(self, fuzzy_knowlage_base: FuzzySearch):
        self.userBase = UserBase()
        self.person = None
        self._chatbot = Chat(pairs, reflections)
        self.fuzzy_knowlage_base = fuzzy_knowlage_base
        self.chatterbot = ChatBot('Tom Riddle',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3',
            read_only=True,
            logic_adapters=[
                # 'chatterbot_adapters.KnowlageBaseAdapter'
                # {
                #     'import_path': 'chatterbot_adapters.KnowlageBaseAdapter'
                # },
                'chatterbot.logic.MathematicalEvaluation',
                # 'chatterbot.logic.TimeLogicAdapter',
                'chatterbot.logic.BestMatch'
        ])

    def respond(self, inp: str, user_id: str):
        res = self._chatbot.respond(inp)
        if res.startswith("[[KNOWLAGE_BASE]]="): 
            res = self.fuzzy_knowlage_base.find(res[len("[[KNOWLAGE_BASE]]="):])
            print("DEBUG: ", res[0], res[2])
            if res[2] < 35: # Confidence threshhold
                res = "You speak nonsense"
            else: #join the sentences together
                res = res[1]["summary"]
        elif res.startswith("[[PERSON.SETHOUSE]]="): 
            house = res[len("[[PERSON.SETHOUSE]]="):]
            
            #get method
            user = self.userBase.get(user_id)
            #modify user class
            user.house = house
            #run the update mehtod 
            self.userBase.update(user_id, user)
            if user.house == None:
                res = "You waste my time. That is not a house fool!"
            elif user.house in ["Gryffindor", "Hufflepuff", "Ravenclaw"]:
                res = "You filthy blood traitor!"
            else:
                res = "Finally, someone worth talking to."
                
            #conditional response
            
        elif res.startswith("[[PERSON.SETNAME]]="):
            user_name = res[len("[[PERSON.SETNAME]]="):]

            user = self.userBase.get(user_id)
            user.name = user_name
            self.userBase.update(user_id, user)

            res = "Nice to meet you " + user_name + ", I'll see if you're worth my time!"
            
        
        elif res.startswith("[[PERSON.SETHOBBY]]="):
            user_hobby = res[len("[[PERSON.SETHOBBY]]="):]

            user = self.userBase.get(user_id)
            user.hobby = user_hobby
            self.userBase.update(user_id, user)

            res = "Ahh I see that you like " + user_hobby 
        
        elif res.startswith("[[PERSON.SETCHAR]]="):
            user_char = res[len("[[PERSON.SETCHAR]]="):]

            user = self.userBase.get(user_id)
            user.characteristic = user_char
            self.userBase.update(user_id, user)

            res = "Ahh " + user_char + ", if only he was loyel..."

        # get person name
        elif res == "[[PERSON.GETNAME]]":
            # get the user name
            user = self.userBase.get(user_id)
            if user.name != None:
                res = "You are " + user.name
            else: 
                res = "You haven't told me yet... "
        # get person house
        elif res == "[[PERSON.GETHOUSE]]":
            # get the user name
            user = self.userBase.get(user_id)
            if user.name != None:
                if user.house == "Slytherine":
                    res = "Ofcourse I remember you, you are true believer!"
                else:
                    res = "Ohh you are from " + user.house + ", you are not worth my time!"
            else:
                res = "You haven't told me yet... "

        # get person char
        elif res == "[[PERSON.GETCHAR]]":
            # get the user name
            user = self.userBase.get(user_id)
            if user.name != None:
                res = "Your friend's with " + user.characteristic
            else:
                res = "You haven't told me yet... "

        # get person hobby
        elif res == "[[PERSON.GETHOBBY]]":
            # get the user name
            user = self.userBase.get(user_id)
            if user.name != None:
                res = "You like to " + user.hobby
            else:
                res = "You haven't told me yet... "

        else:
            res = self.chatterbot.get_response(res).text
        
        return res

    # WILL START A TEXT BASED CHATBOT
    def startTerminalChat(self, user_id):
        
    
        while True:
            inp = input("> ")
            
            # process Response
            res = self.respond(inp, user_id)
            print(res)

            # check for commands
            if inp == "quit":
                break




pairs = (
    (
        r"Tell me about (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
        
    ),

    (
        r"who was (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
        
    ),
    (
        r"how does(.*)work",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
        
    ),
    (
        r"how do you use(.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
        
    ),
    (
        r"Who is (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
    ),
    (
        r"what happened with (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
    ),
    (
        r"what happened to (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
    ),
    (
        r"what do you know about (.*)",
        (
            "[[KNOWLAGE_BASE]]=%1",
            "[[KNOWLAGE_BASE]]=%1"
        ),
    ),

    #Person stuff 
    # house 
    (
        r"my house is (.*)",
        (
            "[[PERSON.SETHOUSE]]=%1",
            "[[PERSON.SETHOUSE]]=%1"
        ),
    ),
    (
        r"i am in (.*)",
        (
            "[[PERSON.SETHOUSE]]=%1",
            "[[PERSON.SETHOUSE]]=%1"
        ),
        
    ),
    #Name
    (
        r"my name is (.*)",
        (
            "[[PERSON.SETNAME]]=%1",
            "[[PERSON.SETNAME]]=%1"
        ),
    ),
    (
        r"I am (.*)",
        (
            "[[PERSON.SETNAME]]=%1",
            "[[PERSON.SETNAME]]=%1"
        ),
    ),
    #hobby
    (
        r"my hobbies are (.*)",
        (
            "[[PERSON.SETHOBBY]]=%1",
            "[[PERSON.SETHOBBY]]=%1"
        ),
    ),
    (
        r"i like to (.*)",
        (
            "[[PERSON.SETHOBBY]]=%1",
            "[[PERSON.SETHOBBY]]=%1"
        ),
    ),
     #Characteristic (Who is their fav person / Who is their friend)
    (
        r"my favorite person is (.*)",
        (
            "[[PERSON.SETCHAR]]=%1",
            "[[PERSON.SETCHAR]]=%1"
        ),
    ),
    (
        r"my friend is (.*)",
        (
            "[[PERSON.SETCHAR]]=%1",
            "[[PERSON.SETCHAR]]=%1"
        ),
    ),
    
    # Read from user data
    #Name
    (
        r"do you know who i am(.*)",
        (
            "[[PERSON.GETNAME]]",
            "[[PERSON.GETNAME]]"
        ),
    ),
    (
        r"whats my name(.*)",
        (
            "[[PERSON.GETNAME]]",
            "[[PERSON.GETNAME]]"
        ),
    ),
    (
        r"what about my name(.*)",
        (
            "[[PERSON.GETNAME]]",
            "[[PERSON.GETNAME]]"
        ),
    ),
    # Read from House
    (
        r"do you know my house(.*)",
        (
            "[[PERSON.GETHOUSE]]",
            "[[PERSON.GETHOUSE]]"
        ),
    ),
    (
        r"whats my house(.*)",
        (
            "[[PERSON.GETHOUSE]]",
            "[[PERSON.GETHOUSE]]"
        ),
    ),
    (
        r"what about my house(.*)",
        (
            "[[PERSON.GETHOUSE]]",
            "[[PERSON.GETHOUSE]]"
        ),
    ),
    # read from char
(
        r"do you know my friend(.*)",
        (
            "[[PERSON.GETCHAR]]",
            "[[PERSON.GETCHAR]]"
        ),
    ),
    (
        r"whats my friend(.*)",
        (
            "[[PERSON.GETCHAR]]",
            "[[PERSON.GETCHAR]]"
        ),
    ),
    (
        r"what about my friend(.*)",
        (
            "[[PERSON.GETCHAR]]",
            "[[PERSON.GETCHAR]]"
        ),
    ),
    # read from hobbies
(
        r"do you know what i like to do(.*)",
        (
            "[[PERSON.GETHOBBY]]",
            "[[PERSON.GETHOBBY]]"
        ),
    ),
    (
        r"whats my favorite thing to do(.*)",
        (
            "[[PERSON.GETHOBBY]]",
            "[[PERSON.GETHOBBY]]"
        ),
    ),
    (
        r"what about my hobbies(.*)",
        (
            "[[PERSON.GETHOBBY]]",
            "[[PERSON.GETHOBBY]]"
        ),
    ),


    ( # Chatterbot 
        r"(.*)",
        (
            "%1",
            "%1"
        ),
    ),
    
)



def main():
    user_id = "1234532454366534543543"
    with open('knowledge_base.pickle', 'rb') as handle:
        knowlage_base = pickle.load(handle)
    search = FuzzySearch(knowlage_base)
    chatbot = TomRiddle(search)
    chatbot.startTerminalChat(user_id)






    

        


# eliza_chatbot = Chat(pairs, reflections)


# def eliza_chat():
#     print("Therapist\n---------")
#     print("Talk to the program by typing in plain English, using normal upper-")
#     print('and lower-case letters and punctuation.  Enter "quit" when done.')
#     print("=" * 72)
#     print("Hello.  How are you feeling today?")

#     eliza_chatbot.converse()



# def demo():
#     eliza_chat()



if __name__ == "__main__":
    # demo()
    main()