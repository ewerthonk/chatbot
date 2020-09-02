import logging 
from chatbot import MeuChatBot
from flask import Flask, render_template , request

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

chatbot = MeuChatBot('Oscar')



app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("index2.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(chatbot.get_response(userText)) 

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="192.168.1.20", port=5002)