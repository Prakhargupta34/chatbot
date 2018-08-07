from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import codecs
app = Flask(__name__)

chatbot = ChatBot('Chandler')
chatbot.set_trainer(ListTrainer)

file=codecs.open('chandler.yml','r+',encoding='utf-8',errors='ignore').readlines()
chatbot.train(file)

file=open('conversations.yml','r+').readlines()
chatbot.train(file)
file=open('greetings.yml','r+').readlines()
chatbot.train(file)

file=open('greetings.yml','r+').readlines()
chatbot.train(file)
file=codecs.open('chandler.yml','r+',encoding='utf-8',errors='ignore').readlines()
chatbot.train(file)

@app.route("/")
def home():
	return render_template("index.html")
@app.route("/get") 
def get_bot_response(): 
	message=request.args.get('msg')
	response=str(chatbot.get_response("%s"%message))
	response=response.replace("- ","")
	return response

if (__name__ == "__main__"): 
    app.run(host = '0.0.0.0',port=80) 
