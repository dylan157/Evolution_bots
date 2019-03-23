from random import randint
from sys import platform
import os
import time
import subprocess
from MapPhysics import MapPhysics
from Botlogic import Botlogic
from Botbuilder import Botbuilder
os.system("mode con: cols=185 lines=125")

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

map_object = MapPhysics(45, 35) # mapgen

bot_logic = Botlogic() #ai


for bot in range(1): #Bot gen
    map_object.living_bots.append(Botbuilder(map_object))


while True:

    for bot in map_object.living_bots: #Bot turn

        move = bot_logic.AI(bot, map_object) #bot move choice

        bot.last_move = move

        bot_logic.board_transport(move, bot, map_object) #bot move

        bot_logic.move_results(map_object, bot) #Bot move results

        map_object.playerboard[bot.x][bot.y] = str(bot.hunger) # BOT to playerboard Icon writer

        bot_logic.bot_birth_check(bot, map_object)

        if map_object.time % 5 == 0: bot.hunger -= 1


    map_object.print_board(map_object.playerboard) #printboard

    bot_logic.bot_health_check(map_object) # health check

    time.sleep(0.05)    

    clear()

    map_object.tidy()

    map_object.nature()

    map_object.time += 1












