from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.portuguese')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data['message']

    bot_response =  bot.get_response(user_message).text

    return jsonify({'reponse': bot_response})

if __name__=='__main__':
    app.run(debug=True)
