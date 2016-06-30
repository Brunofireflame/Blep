import time
import random
import datetime
import telepot

"""
A simple bot that accepts two commands:
- /roll : reply with a random integer between 1 and 6, like rolling a dice.
- /time : reply with the current time, like a clock.
INSERT TOKEN below in the code, and run:
$ python diceyclock.py
Ctrl-C to kill.
"""
R6Sattackers = ["Thermite", "Ash", "Fuze", "Glaz", "Montagne", "Twitch", "Blitz", "IQ", "Sledge", "Thactcher", "Buck", "Blackbeard"]
R6Sdefenders = ["Castle", "Pulse", "Kapkan", "Bestchanka", "Rook", "Doc", "Jaeger", "Bandit", "Mute", "Smoke", "Frost", "Valkyrie"]
Killers = ["The Wraith", "The Hillbilly", "The Trapper"]
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'Attack':
		bot.sendMessage (chat_id, random.choice(R6Sattackers))
    elif command == 'Defend':
            bot.sendMessage (chat_id, random.choice(R6Sdefenders))
    elif command == 'Killer':
            bot.sendMessage (chat_id, random.choice(Killers))
    elif command == '/attack':
		bot.sendMessage (chat_id, random.choice(R6Sattackers))
    elif command == '/defend':
            bot.sendMessage (chat_id, random.choice(R6Sdefenders))
    elif command == '/killer':
            bot.sendMessage (chat_id, random.choice(Killers))
    elif command == '/help':
            bot.sendMessage (chat_id, "Commands are /attack or Attack for an R6S attacker, /defend and Defend for an R6S defender, and /killer or Killer for a DBD Killer.")
    elif command == 'Help':
            bot.sendMessage (chat_id, "Commands are /attack or Attack for an R6S attacker, /defend and Defend for an R6S defender, and /killer or Killer for a DBD Killer.") 

bot = telepot.Bot('253544619:AAEt3qQDuYxYJ5IL9hyiPyCAYi1HOx7YCNc')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
