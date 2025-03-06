from chatterbot import ChatBot

bot = ChatBot("Math Bot",logic_adapters = ["chatterbot.logic.MathematicalEvaluation"])

while True:
    user_input = (input("Type math equation to be solved : "))      # need to give spae while entering input
    print("Bot : ",(bot.get_response(user_input)))      