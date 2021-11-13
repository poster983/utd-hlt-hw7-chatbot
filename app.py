import pickle
from flask import Flask
from flask import render_template
from flask import request
from FuzzySearch import FuzzySearch

from tom_riddle import TomRiddle
#import chatbot and knowlagebase
with open('knowledge_base.pickle', 'rb') as handle:
    knowlage_base = pickle.load(handle)
search = FuzzySearch(knowlage_base)
chatbot = TomRiddle(search)

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('book.html')

@app.route("/chat")
def chat():
    message = request.args.get('message', None)
    if message != None:
        res = chatbot.respond(message)
        print(res)
        return res
    else:
        return "Invalid Message", 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)