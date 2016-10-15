# import chatterbot modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# List of chatbot objects
# This is a good idea, right guys?
# Right?
bots = []
# Create the bot, may CandyToast live on
candybot = ChatBot("CandyToast",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    # output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./candy_toast.json"
)
bots.append(candybot)
print("Bot CandyToast is now ready for use.")
# Discord API server bot
api_memer = ChatBot("Wumpus",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    # output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./ratelimit.json"
)
bots.append(api_memer)
print("Bot Wumpus is now ready for use.")
# TIIIIINY amount of training on english corpus
for bot in bots:
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train("chatterbot.corpus.english")

def talk_to_the_dead(message):
    try:
        bot_input = candybot.get_response(message)
        return bot_input
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass

def may_i_speak_to_the_wumpus(message):
    try:
        bot_input = api_memer.get_response(message)
        return bot_input
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass