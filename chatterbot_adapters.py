from chatterbot.logic import LogicAdapter

from FuzzySearch import FuzzySearch
import pickle

with open('knowledge_base.pickle', 'rb') as handle:
    knowlage_base = pickle.load(handle)
    search = FuzzySearch(knowlage_base)

class KnowlageBaseAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.startswith = [
            "tell me about ",
            "who is ",
            "who was ",
            "what happened during ",
            "what is ",
        ]

    def can_process(self, statement):
        query = statement.text.lower()
        for sen in self.startswith:
            if query.find(sen) != -1:
                
                return True
        return False
        if statement.text in startswith:
            print("TRUE")
            return True
        print("False")
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        query = input_statement.text.lower()
        
        for sen in self.startswith:
            ind = query.find(sen)
            if ind != -1:
                
                query = query[len(sen):]
        
        # Randomly select a confidence between 0 and 1
        kb_data = search.find(query)
        # print(kb_data)
        # For this example, we will just return the input as output
        input_statement.text = kb_data[1]["summary"]
        selected_statement = input_statement

        selected_statement.confidence = kb_data[2]

        

        return selected_statement
