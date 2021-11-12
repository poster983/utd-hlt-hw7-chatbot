from chatterbot import ChatBot

bot = ChatBot('Tom Riddle',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    read_only=False,
    logic_adapters=[
        # 'chatterbot_adapters.KnowlageBaseAdapter'
        # {
        #     'import_path': 'chatterbot_adapters.KnowlageBaseAdapter'
        # },
         'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
         'chatterbot.logic.BestMatch'
    ])

while True:
    try:
        bot_input = bot.get_response(input("> "))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break