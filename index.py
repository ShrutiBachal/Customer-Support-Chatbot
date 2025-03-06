from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request    # flask = web framework based on python 

app = Flask(__name__)       # creating flask obj

bot = ChatBot("Customer Service Bot",read_only=False, 

            logic_adapters=[
            {
                "import_path":"chatterbot.logic.BestMatch",
                "default_response":"Sorry no relevant response found!", 
                "maximum_similarity_threshold":0.9      # if for any user input, the response match value is less than 0.9, then default is used
            }
        ])

list_to_train = [
    "Hello! Welcome to XYZ Customer Support. How can I assist you today? 😊",
    "I want to track my order",
    "Sure! Could you please provide your order number?",
    "It's #123456",
    "Let me check... 🔍...Your order #123456 is out for delivery and should arrive by tomorrow. 🚚",
    "Great! Also, I received a damaged product last time.",
    " I'm sorry to hear that. 😞 Could you please provide the order number for the damaged item?",
    "Yes, it's #654321.",
    "Thank you! You can request a replacement or a refund. Which one would you prefer?",
    "I'd like a replacement",
    "Got it! Your replacement request for order #654321 has been processed. You’ll receive a new item within 3-5 business days. 📦",
    "Thank you!",
    " You're welcome! 😊 Is there anything else I can help you with?",
    " No, that’s all",
    "Alright! Have a great day! 🌟"
]

'''list_to_train_1 = [
    "Hello",
    "Hi how may I help you?",
    "I was facing difficulty while accessing my recorded lectures",
    "Are you not able to find them ?",
    "Yeah will you please guide me",
    "Sure you have to navigate to your profile and there you will find the recording section",
    "Ok Thankyou",
    "My pleasure! Happy learning"
]'''

trainer = ListTrainer(bot)
trainer.train(list_to_train)
#trainer.train(list_to_train_1)

'''trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")'''

@app.route("/") # / = on main page
def main():
    return render_template("index.html")    # returning web page

#while(True):        # to keep user active asking many questions
   # user_response = input("User : ")
   # print("Bot : ",bot.get_response(user_response))

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
