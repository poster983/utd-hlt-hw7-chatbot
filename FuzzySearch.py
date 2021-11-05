from thefuzz import process

# * Uses the Levenshtein distance algo along with thefuzz package (fuzzywuzzy) to find the best match for a user's query
class FuzzySearch():
    def __init__(self, dict):
        self.keys = dict.keys()
        self.dict = dict

    # Wil use fuzzy search to find the closest key and will then return (key, value, confidence) or null 
    def find(self, query: str):
        key = process.extractOne(query, self.keys)
        if key == None or key[1] == 0:
            return None
        value = self.dict[key[0]]
        return (key[0], value, key[1])
