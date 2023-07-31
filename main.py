import os
import time
import telebot
from random import randint
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

my_secret = "<<Secret>>"
bot = telebot.TeleBot(my_secret)

vid=["UT12309","UT12308","UT13453","UT12305","UT45856","UT25698","UT45698","UT78945","UT745682","UT512346","UT745640","UT3456728"]
v= ["Manoj","Tushya","Aryan","Alwin_2","Alwin","Som","Cristiano","Prarthana"," Vitthal","Nobody","Megha"]
v1 = [1079530917,1392975612,1950672578,5141152793,1244070092,1070954897,5178562254,1901610330,5290276471,6139389405,870452982]
b = ["Manoj","manoj","Megha","Jayesh","Aryan","Tushya","Alwin_2","Alwin","Som","Cristiano","Prarthana"," Vitthal","Ishan","Jitesh","Unknown1","Unknown2","Naveen","Darshan","Nobody"]
b1 = [1079530917,5574723282,870452982,1068557318,1950672578,1392975612,5141152793,1244070092,1070954897,5178562254,1901610330,5290276471,1322619277,5384410406,1232256257,5384410406,5262473782,
2084157528,6139389405]

def check_that(va1, va2):
    i = 0
    for v in va2:
        if v != va1[i]:
            return False
        i += 1
    return True


@bot.message_handler(regexp="Pick a card")
def card(message):
    suit=["♣️","♦️","♥️","♠️"]
    card=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    k1 = randint(0,2)
    k2 = randint(0,12)
    print(k1)
    bot.send_message(message.chat.id, "Suit:\n"+card[k2]+" of "+suit[k1])


@bot.message_handler(regexp="Magic")
def magic(message):
    mes = bot.send_message(message.chat.id, "reply back with a text: ")
    bot.register_next_step_handler(mes, magic_1)


def magic_1(message):
    for i in range(69):
        time.sleep(5)
        bot.send_message(
            message.chat.id, "Hey " + idtoname(message.chat.id) + "\n" +
            "This is magic message repeater" + "\n" +
            "________________________\n" + message.text)


@bot.message_handler(regexp="toss a coin")
def toss_coin(message):
    num = randint(1, 2)
    if (num == 1):
        bot.send_message(message.chat.id, "Its a head")
    else:
        bot.send_message(message.chat.id, "Its a tail")


@bot.message_handler(regexp="roll a dice")
def roll_dice(message):
    num = randint(1, 6)
    bot.send_message(message.chat.id, str(num))


@bot.message_handler(regexp="pick a random number")
def pick_rand(message):
    mes = bot.send_message(message.chat.id,
                           "Enter the range seprated by space")
    bot.register_next_step_handler(mes, rand_num)


def rand_num(message):
    num1 = message.text[:message.text.index(' ')]
    num2 = message.text[message.text.index(' ') + 1:]
    if num1.isnumeric() and num2.isnumeric() and int(num1) <= int(num2):
        num = randint(int(num1), int(num2))
        bot.send_message(message.chat.id, str(num))
    else:
        bot.send_message(message.chat.id, "Invalid input")


@bot.message_handler(commands=['messagethem'])
def messagethem(message):
    if message.chat.id != v1[0]:
        bot.send_message(message.chat.id, "Acess denied!!")
        return 0
    mes = bot.send_message(
        message.chat.id, "You are about to text as admin\nEnter the message\n")
    bot.register_next_step_handler(mes, message_them)


def message_them(message):
    for i in b1:
        bot.send_message(
            i,
            """🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻❗\n       Message from admin\n❗🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n""" +
            message.text)
        bot.send_message(message.chat.id, "Done")


@bot.message_handler(commands=['commands'])
def command(message):
    bot.send_message(
        message.chat.id,
        "/start -start the convo\n/stop -end the convo\n/text -send anonymous text to anyone\n/register -get yourself registered\n/connections -check all your connections\n/contact -contact the admin\n/info -show my account info\n/play -play a game\n/commands -display all commands available\n\n--------only admin commands----------\n/messagehim -message a person using id\n/messageall -message all registered person\n/messagethem -message all known users\n/knowall -know all known persons\n/knowhim -know a person using his id"
    )


@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(v1[0],
                     str(idtoname(message.chat.id)) + ' : ' + message.text)
    bot.send_message(message.chat.id,
                     "Available games\n1)Guess the number\n2)Tic Tac Toe")
    mes = bot.send_message(message.chat.id, "Reply back with either 1 or 2")
    bot.register_next_step_handler(mes, game_choice)

def check_win(board_deck):
  print("board= ",board_deck)
  for i in range(0,3,6):
    if(board_deck[0+i]==board_deck[1+i] and board_deck[0+i]==board_deck[2+i] and board_deck[0+i] in ['X','O']):
      return True
  for i in range(0,1,2):
    if(board_deck[0+i]==board_deck[3+i] and board_deck[0+i]==board_deck[6+i] and board_deck[0+i] in ['X','O']):
      return True
  for i in range(0,2):
    if(board_deck[0+i]==board_deck[4] and board_deck[0+i]==board_deck[8-i] and board_deck[4] in ['X','O']):
      print("check =",board_deck[0+i],board_deck[4],board_deck[8-i])
      return True
  return False

def check_draw(board_deck):
  for i in range(0,9):
    if board_deck[i] not in ['O','X']:
      return False
  return True

def select_counter(message):
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(*[
        types.InlineKeyboardButton("X", callback_data="select_counterX"),
        types.InlineKeyboardButton("O", callback_data="select_counterO")
    ])
    bot.edit_message_text("Select a place holder:",
                          message.chat.id,
                          message.id,
                          reply_markup=markup)


def computer(update, board_desk, user_placeholder):
    if user_placeholder == "X":
        comp_placeholder = "O"
    else:
        comp_placeholder = "X"
    poss_set = [1, 1, 1, 1, 1, 1, 1, 1]
    board_set = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    for (i, j) in zip(board_desk, range(0, 9)):
        if i != " ":
            if i == comp_placeholder:
                board_set[j] = "C"
            else:
                board_set[j] = "H"
    for i in range(0, 8):
        if i < 3:
            str = board_set[3 * i:(3 * i) + 3]
        elif i < 6:
            str = [board_set[i - 3], board_set[i], board_set[i + 3]]
        else:
            if i == 6:
                str = [board_set[0], board_set[4], board_set[8]]
            elif i == 7:
                str = [board_set[2], board_set[4], board_set[6]]
        if "C" in str and 'H' in str:
            poss_set[i] = -1
        if "C" in str or 'H' in str:
            l1 = 0
            l2 = 0
            for b in str:
                if b == 'C':
                    l1 += 1
                elif b == 'H':
                    l2 += 1
            if l1 > 1 or l2 > 1:
                poss_set[i] = 5
            else:
                poss_set[i] = 3
    for i in range(0, 8):
        if i < 3:
            for l in range(0, 3):
                if board_set[(3 * i) + l] not in ['C', 'H']:
                    board_set[(3 * i) + l] += poss_set[i]
        elif i < 6:
            for l in range(0, 3):
                if board_set[i + 3 * (l - 1)] not in ['C', 'H']:
                    board_set[i + 3 * (l - 1)] += poss_set[i]
        elif i == 6:
            for l in range(0, 3):
                if board_set[l * 4] not in ['C', 'H']:
                    board_set[l * 4] += poss_set[i]
        elif i == 7:
            for l in range(0, 3):
                if board_set[(l + 1) * 2] not in ['C', 'H']:
                    board_set[(l + 1) * 2] += poss_set[i]
    larger = 0
    index = 0
    for (i, j) in zip(board_set, range(0, 9)):
        if isinstance(i, int) and larger < i:
            larger = i
            index = j
    try:
        board_desk = board_desk[:index] + comp_placeholder + board_desk[index +1:]
    except:
        board_desk = board_desk[:index] + comp_placeholder
    if check_win(board_desk):
      bot.edit_message_text("Ooooops!! you lost the game!!!😟",
                          update.message.chat.id,
                          update.message.id)
      return 0
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for x in range(0, 9):
        val = "board"+"{}".format(x)+user_placeholder+board_desk
        button = types.InlineKeyboardButton(board_desk[x], callback_data=val)
        buttons.append(button)
    markup.add(*buttons)
    bot.edit_message_text("Board:",
                          update.message.chat.id,
                          update.message.id,
                          reply_markup=markup)
    return board_desk


@bot.callback_query_handler(lambda update: check_that(update.data, "board"))
def board_play(update):
    key=1
    board_desk = update.data[7:]
    if board_desk[int(update.data[5:6])] != " ":
        return 0
    index = int(update.data[5:6])
    user_placeholder = update.data[6:7]
    try:
        board_desk = board_desk[:index] + user_placeholder + board_desk[index +1:]
    except:
        board_desk = board_desk[:index] + user_placeholder
    if check_win(board_desk):
      bot.edit_message_text("Congrats, you won the game!!!🥳🥳",
                          update.message.chat.id,
                          update.message.id)
      key=0
      return 0
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for x in range(0, 9):
        button = types.InlineKeyboardButton(board_desk[x],
                                            callback_data="board" + str(x) +
                                            user_placeholder + board_desk)
        buttons.append(button)
    markup.add(*buttons)
    bot.edit_message_text("Board:",
                          update.message.chat.id,
                          update.message.id,
                          reply_markup=markup)
    if(key==1):
        computer(update, board_desk, user_placeholder)


@bot.callback_query_handler(
    lambda update: check_that(update.data, 'select_counter'))
def select_cou(update):
    print(update.data[14:])
    board_desk = "         "
    markup = InlineKeyboardMarkup(row_width=3)
    #remember 0 is human and 1 is computer
    num = randint(0, 1)
    if (num == 0):
        place_hold = "You won the toss"
    else:
        place_hold = "You lost the toss"
        board_desk = computer(update, board_desk, update.data[14:])
    buttons = []
    for x in range(0, 9):
        button = types.InlineKeyboardButton(board_desk[x],
                                            callback_data="board" + str(x) +
                                            update.data[14:] + board_desk)
        buttons.append(button)
    markup.add(*buttons)
    bot.edit_message_text("Tossing a coin....\n" + place_hold +
                          "\nMake your move\nBoard:",
                          update.message.chat.id,
                          update.message.id,
                          reply_markup=markup)


def play_1(message):
    print("hello")
    select_counter(message)


def game_2(message):
    mes = bot.send_message(message.chat.id, "loading....")
    print("hello2")
    play_1(mes)


def game_choice(message):
    if message.text.isnumeric() and int(message.text) in [1, 2]:
        if int(message.text) == 1:
            bot.send_message(
                message.chat.id,
                "Guess the number\n------------------------\nHow to play??\nThis is a number guessing game you just have to guess the number.\n1)Number is between 0 to 10001\n2)You have 12 tries\n3)text stop to end the game\n"
            )
            num = randint(1, 10000)
            count = 0
            mes = bot.send_message(message.chat.id,
                                   "Reply back with your guess!!")
            bot.register_next_step_handler(mes, game_1, num, count + 1)
        else:
            mes = bot.send_message(message.chat.id,
                                   "Tic Tac Toe game is about to start")
            game_2(message)
    else:
        mes = bot.send_message(message.chat.id, "Invalid choice!!")
        bot.register_next_step_handler(mes, game_choice)


def game_1(message, num, count):
    if message.text in ['stop', 'Stop', 'STOP']:
        bot.send_message(message.chat.id,
                         "Bye!!\nHope we see you come back soon...")
        return 0
    if (message.text.isnumeric()):
        if not (int(message.text) > 0 and int(message.text) < 10001):
            mes = bot.send_message(message.chat.id,
                                   "Enter a number between 0 and 10001\n")
            bot.register_next_step_handler(mes, game_1, num, count)
        else:
            if num == int(message.text):
                bot.send_message(
                    message.chat.id,
                    "You won!!\nYou got it right in " + str(count) + " tries")
            elif num > int(message.text):
                mes = bot.send_message(
                    message.chat.id, "Try with a larger number\n[" +
                    str(12 - count) + " tries left]")
                count += 1
                if (count > 12):
                    bot.send_message(message.chat.id,
                                     "No more tries!!\nYou lost\n")
                    return 0
                bot.register_next_step_handler(mes, game_1, num, count)
            else:
                mes = bot.send_message(
                    message.chat.id, "Try with a smaller number\n[" +
                    str(12 - count) + " tries left]")
                count += 1
                if (count > 12):
                    bot.send_message(message.chat.id,
                                     "No more tries!!\nYou lost\n")
                    return 0
                bot.register_next_step_handler(mes, game_1, num, count)
    else:
        mes = bot.send_message(message.chat.id, "Enter a valid number\n")
        bot.register_next_step_handler(mes, game_1, num, count)


@bot.message_handler(commands=['info'])
def info(message):
    if message.chat.id not in v1:
        bot.send_message(
            message.chat.id,
            "Probably you are not yet registered\nYou are missing all the fun\nJust text \register to get registered"
        )
    else:
        but = InlineKeyboardMarkup()
        but.add(InlineKeyboardButton("Edit", callback_data="edit_me"))
        bot.send_message(message.chat.id,
                         "Account info\n----------------------\nUserId: " +
                         str(vid[v1.index(message.chat.id)]) + "\nName: " +
                         v[v1.index(message.chat.id)] + "\nConnection id:" +
                         str(message.chat.id),
                         reply_markup=but)


@bot.message_handler(commands=['knowhim'])
def knowhim(message):
    bot.send_message(v1[0],
                     str(idtoname(message.chat.id)) + ' : ' + message.text)
    if (message.chat.id != v1[0]):
        bot.send_message(message.chat.id, "Access denied!!")
    else:
        msg = bot.send_message(message.chat.id, "Enter chat id: ")
        bot.register_next_step_handler(msg, find_user)


def find_user(message):
    if int(message.text) in b1:
        bot.send_message(message.chat.id, b[b1.index(int(message.text))])
    else:
        bot.send_message(message.chat.id, "Id not found in database!!!")


@bot.message_handler(commands=['knowall'])
def knowall(message):
    if (int(message.chat.id) != v1[0]):
        bot.send_message(message.chat.id, "Acess denied!!")
    else:
        mess = ""
        for (x, y) in zip(b, b1):
            mess += x + " : " + str(y)
            mess += "\n"
        bot.send_message(message.chat.id, mess)


@bot.callback_query_handler(lambda update: update.data == 'edit_me')
def edit_user(update):
    but = InlineKeyboardMarkup()
    but.add(*[
        InlineKeyboardButton("back", callback_data="edit_b"),
        InlineKeyboardButton("Name", callback_data="edit_n"),
        InlineKeyboardButton("userid", callback_data="edit_u")
    ])
    bot.edit_message_text("Account info\n----------------------\nUserId: " +
                          str(vid[v1.index(update.message.chat.id)]) +
                          "\nName: " + v[v1.index(update.message.chat.id)] +
                          "\nConnection id:" + str(update.message.chat.id),
                          update.message.chat.id,
                          update.message.id,
                          reply_markup=but)
    bot.answer_callback_query(update.id)


@bot.callback_query_handler(lambda update: update.data == 'edit_b')
def edit_b(update):
    but = InlineKeyboardMarkup()
    but.add(InlineKeyboardButton("edit", callback_data="edit_me"))
    bot.edit_message_text("Account info\n----------------------\nUserId: " +
                          str(vid[v1.index(update.message.chat.id)]) +
                          "\nName: " + v[v1.index(update.message.chat.id)] +
                          "\nConnection id:" + str(update.message.chat.id),
                          update.message.chat.id,
                          update.message.id,
                          reply_markup=but)
    bot.answer_callback_query(update.id)


@bot.callback_query_handler(lambda update: update.data == 'edit_n')
def edit_n(update):
    bot.send_message(update.message.chat.id, "enter your new name:")
    bot.register_next_step_handler(update.message, he_ll, 1)


@bot.callback_query_handler(lambda update: update.data == 'edit_u')
def edit_u(update):
    bot.send_message(
        update.message.chat.id,
        "enter your new userId:\n(Only numbers are letters are allowed)")
    bot.register_next_step_handler(update.message, he_ll, 2)


def he_ll(message, k):
    if (k == 1):
        bot.send_message(
            v1[0],
            str(message.chat.id) + ": " + "Update my name:\n" + "from " +
            v[v1.index(message.chat.id)] + "\nto " + message.text)
        v[v1.index(message.chat.id)] = message.text
        bot.send_message(message.chat.id, "done")
    elif (k == 2):
        try:
            vid.index(message.text)
            bot.send_message(message.chat.id, "not available\ntry again!!")
            bot.send_message(
                message.chat.id,
                "enter your new userId:\n(Only numbers are letters are allowed)"
            )
            bot.register_next_step_handler(message, he_ll, 2)
        except Exception:
            bot.send_message(
                v1[0],
                str(message.chat.id) + ": " + "Update my userid:\n" + "from " +
                vid[v1.index(message.chat.id)] + "\nto " + message.text)
            vid[v1.index(message.chat.id)] = message.text
            bot.send_message(message.chat.id, "done")


@bot.message_handler(commands=['connections'])
def connections(message):
    bot.send_message(message.chat.id, "Currently under development!!")


@bot.message_handler(commands=['messagehim'])
def mes(message):
    if (message.chat.id == v1[0]):
        msg = bot.send_message(message.chat.id, "Enter his id:")
        bot.register_next_step_handler(msg, text_him)
    else:
        bot.send_message(message.chat.id, "Access denied!!")


def text_him(message):
    msg = bot.send_message(message.chat.id, "enter a message to forward:")
    bot.register_next_step_handler(msg, text_h, message.text)


def text_h(message, id):
    try:
        bot.send_message(message.chat.id, "done")
        bot.send_message(
            id,
            """🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻❗\n       Message from admin\n❗🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n""" +
            message.text)
    except Exception:
        bot.reply_to(message, "Oooops!\ntry again..")


@bot.message_handler(commands=['contact'])
def conta_admin(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(*[
        InlineKeyboardButton('DM', url='https://telegram.me/mdaonr'),
        InlineKeyboardButton('message', callback_data='text_him' + str(v1[0]))
    ])
    bot.send_message(
        message.chat.id,
        "Contact admin\nText admin at @mdaonr\nor text him as a stranger",
        reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(v1[0], idtoname(message.chat.id) + ": " + message.text)
    global mag
    bot.send_message(message.chat.id, "Hey! Welcome\n")
    make = InlineKeyboardMarkup()
    make.add(
        InlineKeyboardButton('Know how it works!!', callback_data='process'))
    mag = bot.send_message(
        message.chat.id,
        'Important:-\nNo messages can be stored anywhere, messages can\'t even be accessed by the owner himself. It\'s just you who know your messages',
        reply_markup=make)
    bot.send_message(message.chat.id, "Author:-Manoj Patil(@mdaonr)")


@bot.callback_query_handler(lambda update: update.data == 'process')
def first_handler(update):
    make = InlineKeyboardMarkup()
    make.add(InlineKeyboardButton('Back', callback_data='proc_back'))
    bot.edit_message_text(
        'Working:-\n•texting /text will display the list of registered names\n•Click on the name and respond back with the message you wanna send\n♦Also u can enter /register to get registered',
        update.message.chat.id,
        update.message.id,
        reply_markup=make)
    bot.answer_callback_query(update.id)


@bot.callback_query_handler(lambda update: update.data == 'proc_back')
def back_handler(update):
    global mag
    make = InlineKeyboardMarkup()
    make.add(
        InlineKeyboardButton('Know how it works!!', callback_data='process'))
    global chat_id
    bot.edit_message_text(
        'Important:-\nNo messages can be stored anywhere, messages can\'t even be accessed by the owner himself. It\'s just you who know your messages ',
        update.message.chat.id,
        update.message.id,
        reply_markup=make)
    bot.answer_callback_query(update.id)


@bot.message_handler(commands=['register'])
def register(message):
    for x in v1:
        if (x == message.chat.id):
            bot.send_message(
                message.chat.id,
                "Ooops!!\nIt looks like you are already registered as " +
                v[v1.index(x)])
            return 0
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Register", callback_data="register"))
    bot.send_message(
        message.chat.id,
        'By getting yourself registered you agree that anystrange can contact you via this bot',
        reply_markup=markup)


@bot.callback_query_handler(lambda update: update.data == 'register')
def reg(update):
    msg = bot.send_message(update.message.chat.id, "Enter your name:-")
    bot.register_next_step_handler(msg, register_user)


def register_user(message):
    bot.reply_to(
        message,
        "You are done!!\nThats all we need, to get you registered\nWe will get back to you soon..."
    )
    print(message.text + ":" + str(message.chat.id))
    bot.send_message(
        v1[0], "application\n" + "name: " + message.text + "\nId: " +
        str(message.chat.id))


@bot.message_handler(commands=['messageall'])
def die(message):
    if (message.chat.id == v1[0]):
        markup = types.InlineKeyboardMarkup(row_width=3)
        buttons = []
        button = types.InlineKeyboardButton("All",
                                            callback_data="admin_text_all")
        buttons.append(button)
        for (x, y) in zip(v, v1):
            button = types.InlineKeyboardButton(x,
                                                callback_data="admin_text" +
                                                str(y))
            buttons.append(button)
        markup.add(*buttons)
        bot.send_message(message.chat.id,
                         "You are about to message as admin!!",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Access denied!!")


@bot.callback_query_handler(lambda update: update.data == 'admin_text_all')
def admin_text_all(update):
    msg = bot.send_message(update.message.chat.id, "Enter a message:")
    bot.register_next_step_handler(msg, text_all)


def text_all(message):
    for x in v1:
        bot.send_message(v1[0], "Done")
        bot.send_message(
            x,
            """🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻❗\n       Message from admin\n❗🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n""" +
            message.text)


@bot.callback_query_handler(
    lambda update: check_that(update.data, 'admin_text'))
def admin_text(update):
    id = get_id(update.data, 'admin_text')
    msg = bot.send_message(update.message.chat.id, "Enter a message:")
    bot.register_next_step_handler(msg, text_admin, id)


def text_admin(message, id):
    bot.send_message(v1[0], "Done")
    bot.send_message(
        id, """🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻❗\n       Message from admin\n❗🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n""" +
        message.text)


@bot.message_handler(commands=['text'])
def play(message):
    bot.send_message(v1[0], idtoname(message.chat.id) + ": " + message.text)
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for (x, y) in zip(v, v1):
        button = types.InlineKeyboardButton(x,
                                            callback_data="text_him" + str(y))
        buttons.append(button)
    markup.add(*buttons)
    bot.send_message(message.chat.id,
                     "Select a person to text:",
                     reply_markup=markup)


def get_id(a, b):
    i = 0
    j = 0
    for v in a:
        if len(b) <= i:
            j = (j * 10) + int(v)
        i += 1
    return j


@bot.callback_query_handler(lambda update: check_that(update.data, 'text_him'))
def name_text(update):
    id = get_id(update.data, 'text_him')
    msg = bot.send_message(update.message.chat.id, "Enter a text to forward")
    bot.register_next_step_handler(msg, mes_send, id)


def mes_send(message, id):
    try:
        bot.reply_to(message, 'Done')
        bot.send_message(v1[0],
                         idtoname(message.chat.id) + ": " + message.text)
        markup = types.InlineKeyboardMarkup()
        markup.add(*[
            types.InlineKeyboardButton(
                'Reply', callback_data="text_him" + str(message.chat.id)),
            types.InlineKeyboardButton('Report',
                                       callback_data="report_this" + "[" +
                                       str(message.chat.id) + "_" + str(id) +
                                       "]" + message.text)
        ])
        bot.send_message(id,
                         "<b>Stranger:</b>\n" + message.text,
                         reply_markup=markup,
                         parse_mode='HTML')

    except Exception:
        bot.reply_to(message, 'oooops try again')


def str_up(a):
    k = 0
    l = True
    m = True
    new_a = "from: "
    for i in a:
        if (i == ']' and m):
            m = False
            new_a = new_a + "\n"
        elif ((i == '_' and l)):
            l = False
            new_a = new_a + "\nto: "
        elif (k != 0):
            new_a = new_a + i
        k += 1
    return new_a


@bot.callback_query_handler(
    lambda update: check_that(update.data, 'report_this'))
def report(update):
    va = str_up(update.data.replace('report_this', ''))
    print(va)
    bot.send_message(v1[0], "Report received!!\nDetails:-\n" + va)
    bot.send_message(update.message.chat.id,
                     "Report submited👍\nadmin will get back to you soon..")


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(1079530917,
                     idtoname(message.chat.id) + ": " + message.text)
    bot.send_message(message.chat.id, "bye! See you soon...")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(
        message,
        "Oooop!!\nMaybe you need some help\ntry entering /start\nIt might help you"
    )
    bot.send_message(1079530917,
                     idtoname(message.chat.id) + ": " + message.text)


def idtoname(num):
    try:
        return b[b1.index(num)]
    except Exception:
        return str(num)


bot.polling()
